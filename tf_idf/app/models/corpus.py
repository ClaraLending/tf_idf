import math

from nltk.corpus import gutenberg as nltk_gutenberg_corpus

from .document import Document


class Corpus(object):
    
    def __init__(self, documents):
        documents = {}
        for title, words in documents.items():
            document = Document(title, words)
            documents[title] = document
        self._documents = documents
        
        self._words = {}

        # @TODO:
        # implement document word count
        # hint: use the collections.Counter class
        # self._words should be a dict mapping each word to a CorpusWordStatistics object

    @property
    def documents(self):
        return self._documents
        
    @property
    def words(self):
        return self._words


class CorpusWordStatistics(object):
    
    def __init__(self, word, document_count, corpus):
        self._word = word
        self._document_count = document_count
        self._corpus = corpus
    
    @property
    def idf_boolean(self):
        return math.log(len(self._corpus.documents) / (1 + self._document_count))
    
    @property
    def tf_idf_linear_boolean(self, document_title):
        return self._corpus.documents[document_title].words[self._word].tf_linear * self.idf_boolean


class NLTKGutenbergCorpus(Corpus):
    
    def __init__(self):
        documents = {}
        for title in nltk_gutenberg_corpus.fileids():
            documents[title] = nltk_gutenberg_corpus.words(title)
        super().__init__(documents)
