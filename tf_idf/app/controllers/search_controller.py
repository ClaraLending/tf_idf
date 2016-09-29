from flask import render_template
from flask import request


class SearchController(object):

    def __init__(self, search_engine):
        self._search_engine = search_engine

    def index(self):
        return '''
            <form action="./search_results" method="GET">
                <span>Search:&nbsp;</span>
                <input type="text" name="args">
                <input type="submit" value="Search">
            </form>
        '''
    
    def results_index(self):
        args = request.args.get('args')
        results = self._search_engine.search_by_word(args)
        return render_template('search_results_view.html', results=results)
