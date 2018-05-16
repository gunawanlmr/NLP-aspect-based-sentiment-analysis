class similarity:
    def __init__(self):
        corpus = getTweetData()
        self.model = self.getWord2Vec(corpus)
        self.aspects = ['makanan', 'pelayanan', 'harga', 'suasana']
        self.polarities = ['positif', 'negatif']
        
    def getWord2Vec(self, toFeed, dim=50):
        return gensim.models.Word2Vec(toFeed, min_count=1,  size=dim)
    
    def most_similar_aspect(self, word):
        most_similar = (0, "")
        for aspect in self.aspects:
            score = self.model.wv.similarity(word, aspect)
            if score > most_similar[0]:
                most_similar = (score, aspect)
        return most_similar
    
    def most_similar_polarities(self, word):
        most_similar = (0, "")
        for polarity in self.polarities:
            score = self.model.wv.similarity(word, polarity)
            if score > most_similar[0]:
                most_similar = (score, polarity)
        return most_similar