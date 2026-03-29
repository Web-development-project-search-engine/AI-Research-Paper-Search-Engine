from sklearn.metrics.pairwise import cosine_similarity
from search.vectorizer import PaperVectorizer

class SearchEngine:

    def __init__(self):
        self.vectorizer = PaperVectorizer()
        self.vectorizer.build_index()

    def search(self, query, top_k=5):

        embeddings = self.vectorizer.get_embeddings()
        papers = self.vectorizer.get_papers()

        query_vector = self.vectorizer.encode_query(query)

        similarity = cosine_similarity(query_vector, embeddings)

        ranked_indices = similarity.argsort()[0][::-1]

        print("Top indices:", ranked_indices[:top_k])

        results = []

        for i in ranked_indices[:top_k]:
            results.append(papers[i]) 

        return results