from ..app.controllers.root_controller import RootController
from ..app.controllers.calculations_controller import CalculationsController
from ..app.controllers.search_controller import SearchController

def routes(app, corpus, search_engine):

    root_controller = RootController()
    calculations_controller = CalculationsController(corpus)
    search_controller = SearchController(search_engine)

    app.add_url_rule('/', 'root__index', root_controller.index)
    app.add_url_rule('/calculations', 'calculations__index', calculations_controller.index)
    app.add_url_rule('/search', 'search__index', search_controller.index)
    app.add_url_rule('/search_results', 'search_results__index', search_controller.results_index)
