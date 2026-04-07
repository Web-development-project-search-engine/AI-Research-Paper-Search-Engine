from sentence_transformers import SentenceTransformer
from database.db import get_all_papers
import numpy as np

class PaperTransformer:

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = None
        self.papers = []

    def build_index(self):
        self.papers = get_all_papers()

        # embeddings already stored in DB
        self.embeddings = np.array([paper["embedding"] for paper in self.papers])

        print("Transformers built successfully")

    def encode_query(self, query):
        return self.model.encode([query])

    def get_embeddings(self):
        return self.embeddings

    def get_papers(self):
        return self.papers
    
    def compute_similarity(self, query):
        query_embedding = self.encode_query(query)[0]

        # cosine similarity
        scores = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )

        return scores