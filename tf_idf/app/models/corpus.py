from nltk.corpus import gutenberg as nltk_gutenberg_corpus

from .document import Document


class Corpus(object):
    
    def __init__(self, documents):
        documents = {}
        for title, words in documents.items():
            document = Document(title, words)
            documents[title] = document
        self._documents = documents

    @property
    def documents(self):
        return self._documents


class NLTKGutenbergCorpus(Corpus):
    
    def __init__(self):
        documents = {}
        for title in nltk_gutenberg_corpus.fileids():
            documents[title] = nltk_gutenberg_corpus.words(title)
        super().__init__(documents)
