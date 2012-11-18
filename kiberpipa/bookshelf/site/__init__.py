def includeme(config):
    config.add_static_view('static', 'kiberpipa.bookshelf.site:static')
    config.add_jinja2_search_path("kiberpipa.bookshelf.site:templates")
    config.add_route('book', '/book/{id}')
    config.add_route('search_results', '/')
    config.scan('.')
