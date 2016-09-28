from flask import render_template


class CalculationsController(object):

    def __init__(self, corpus):
        self._corpus = corpus

    def index(self):
        return render_template('calculations_view.html', corpus=self._corpus)
