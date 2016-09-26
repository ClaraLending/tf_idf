from ..app.controllers import root_controller
from ..app.controllers import calculations_controller

def routes(app):
    
    app.add_url_rule('/', 'root__index', root_controller.index)

    app.add_url_rule('/calculations', 'calculations__index', calculations_controller.index)
