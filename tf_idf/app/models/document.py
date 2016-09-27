import collections


class Document(object):
    
    def __init__(self, title, words):
        self._title = title
        
        self._word_count = 0
        self._words = {}
        
        # @TODO:
        # implement word count
        # hint: use the collections.Counter class
        # self._word_count should be the total number of words
        # self._words should be a dict mapping each word to a DocumentWordStatistics object
        counter = collections.Counter(words)
        for word, word_count in counter.items():
            self._words[word] = DocumentWordStatistics(word_count, self)
            self._word_count += word_count

    @property
    def title(self):
        return self._title

    @property
    def word_count(self):
        return self._word_count
        
    @property
    def words(self):
        return self._words


class DocumentWordStatistics(object):
    
    def __init__(self, count, document):
        self._count = count
        self._document = document
    
    @property
    def count(self):
        return self._count
    
    @property
    def tf_linear(self):
        return self._count / self._document.word_count
