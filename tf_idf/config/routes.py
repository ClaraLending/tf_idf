from ..app.controllers.root_controller import RootController
from ..app.controllers.calculations_controller import CalculationsController

def routes(app, corpus):

    root_controller = RootController()
    calculations_controller = CalculationsController(corpus)

    app.add_url_rule('/', 'root__index', root_controller.index)
    app.add_url_rule('/calculations', 'calculations__index', calculations_controller.index)
