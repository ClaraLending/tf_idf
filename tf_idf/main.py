import os

from flask import Flask

from .app.models.corpus import NLTKGutenbergCorpus
from .config.routes import routes

corpus = NLTKGutenbergCorpus()

app = Flask(__name__)
routes(app, corpus)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
