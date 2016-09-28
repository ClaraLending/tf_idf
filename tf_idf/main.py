import os

from flask import Flask

from .app.models.corpus import NLTKGutenbergCorpus
from .config.routes import routes

corpus = NLTKGutenbergCorpus()

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'views'))
routes(app, corpus)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
