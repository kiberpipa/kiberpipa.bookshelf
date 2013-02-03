import logging
import simplejson
import ordereddict

from pysolr import Solr
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from webhelpers.number import format_byte_size

import iptools


log = logging.getLogger(__name__)

# use ordered dict to keep sorted order for faceted values
decoder = simplejson.JSONDecoder(object_pairs_hook=ordereddict.OrderedDict)


@view_config(route_name="book", renderer='book.jinja2')
def book(request):
    # TODO: based on md5, find the book in solr and display all the data
    return {}


@view_config(route_name="search_results", renderer='search_results.jinja2')
@view_config(route_name="search_results_json", renderer='json')
def search_results(request):
    conn = Solr(request.registry.settings['solr_base_url'], decoder=decoder)
    params = request.GET.copy()
    q = params.pop('q', None)
    if q is None:
        return HTTPFound('http://2012.haip.cc/')

    params.update({
        'facet': 'true',
        'facet.limit': 20,
        'facet.mincount': 1,
        'facet.sort': 'count',
        'facet.field': ['language', 'author_exact', 'year'],
        'fl': '*',
    })

    # TODO: get cover data, description from
    # https://developers.google.com/books/docs/v1/reference/volumes
    # TODO: refactor logic from template to view
    # TODO: tests

    # first do request without fq so we get all facet values
    params_temp = params.copy()
    if 'fq' in params_temp:
        del params_temp['fq']
    facet_fields = conn.search(q, **params_temp).facets['facet_fields']

    # workaround due to limitation that kwargs can't handle multidict
    if 'fq' in params:
        params['fq'] = ' AND '.join(params.getall('fq'))

    log.debug(params)
    results = conn.search(q, **params)
    log.debug(results)

    allowed_networks = request.registry.settings['allowed_networks'].split(',')
    if request.client_addr.startswith('::ffff:'):
        ip = request.client_addr[len('::ffff:'):]
    else:
        ip = request.client_addr
    if ip in iptools.IpRangeList(*allowed_networks):
        is_trusted_ip = True
    else:
        is_trusted_ip = False

    out = {
        'results': list(results),
        'q': q,
        'facet_fields': facet_fields,
        'facets': params.get('fq', []),
    }

    if request.matched_route.name.endswith('json'):
        return out
    else:
        out.update({
            'with_facet': with_facet,
            'without_facet': without_facet,
            'format_byte_size': format_byte_size,
            'format_facet': format_facet,
            'is_trusted_ip': is_trusted_ip,
        })
        return out


def with_facet(request, facet, value):
    query = request.GET.copy()
    query['fq'] = [f for f in query.getall('fq') if not f.startswith(facet)]
    query.add('fq', format_facet(facet, value))
    return request.current_route_url(_query=query)


def without_facet(request, facet):
    query = request.GET.copy()
    query['fq'] = [f for f in query.getall('fq') if not f.startswith(facet)]
    return request.current_route_url(_query=query)


def format_facet(facet, value):
    return '%s:"%s"' % (facet, value)
