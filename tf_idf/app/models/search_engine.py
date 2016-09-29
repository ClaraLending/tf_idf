class SearchEngine(object):
    
    def __init__(self, corpus):
        self._corpus = corpus
        
    def search_by_word(self, word, offset=0, count=25):
        # @TODO: implement the search algorithm
        # put the results into the results list
        if word not in self._corpus.words:
            return []
        document_scores = []
        for document_title, document in self._corpus.documents.items():
            score = self._corpus.words[word].tf_idf_linear_boolean(document_title)
            if score > 0.000001:
                document_scores.append((score, document))
        document_scores = sorted(document_scores, key=lambda x: x[0])
        results = [x[1] for x in document_scores]
        return results
