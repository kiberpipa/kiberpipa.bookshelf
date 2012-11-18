from pysolr import Solr
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


SOLR_BASE_URL = 'http://127.0.0.1:8983/solr/en'


@view_config(route_name="book", renderer='book.jinja2')
def book(request):
    # TODO: based on md5, find the book in solr and display all the data
    return {}


@view_config(route_name="search_results", renderer='search_results.jinja2')
def search_results(request):
    conn = Solr(SOLR_BASE_URL)
    q = request.GET.get('q', None)
    if q is None:
        return HTTPFound('http://2012.haip.cc/')
    results = conn.search(q)
    return {'results': results, 'q': q}
