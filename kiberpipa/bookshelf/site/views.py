import simplejson
import ordereddict

from pysolr import Solr
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from webhelpers.number import format_byte_size


SOLR_BASE_URL = 'http://127.0.0.1:8984/solr/en'

# use ordered dict to keep sorted order for faceted values
decoder = simplejson.JSONDecoder(object_pairs_hook=ordereddict.OrderedDict)


@view_config(route_name="book", renderer='book.jinja2')
def book(request):
    # TODO: based on md5, find the book in solr and display all the data
    return {}


@view_config(route_name="search_results", renderer='search_results.jinja2')
def search_results(request):
    conn = Solr(SOLR_BASE_URL, decoder=decoder)
    params = request.GET.copy()
    q = params.pop('q', None)
    if q is None:
        return HTTPFound('http://2012.haip.cc/')

    params.update({
        'facet': 'true',
        'facet.limit': 20,
        'facet.mincount': 5,
        'facet.sort': 'count',
        'facet.field': ['language', 'author_exact', 'year'],
        'fl': '*',
    })
    results = conn.search(q, **params)
    return {
        'results': results,
        'q': q,
        'with_facet': with_facet,
        'format_byte_size': format_byte_size,
    }


def with_facet(request, facet, value):
    query = request.GET.copy()
    query.add('fq', '%s:"%s"' % (facet, value))
    return request.current_route_url(_query=query)
