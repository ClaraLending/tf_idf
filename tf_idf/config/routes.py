from ..app.controllers import root_controller

def routes(app):
    
    app.route('/')(root_controller.index)
