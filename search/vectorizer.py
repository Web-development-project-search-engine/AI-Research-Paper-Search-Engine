from sentence_transformers import SentenceTransformer
from database.db import get_all_papers
import numpy as np

class PaperVectorizer:

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = None
        self.papers = []

    def build_index(self):
        # load papers from mongodb
        self.papers = get_all_papers()


        for paper in self.papers:
            text = (
                        paper.get("cleaned_title", "") * 3 + " " +
                        paper.get("cleaned_abstract", "") + " " +
                        paper.get("cleaned_authors", "")
                    )

        # store embeddings
        self.embeddings = np.array([paper["embedding"] for paper in self.papers])

        print("Transformers built successfully")

    def encode_query(self, query):
        return self.model.encode([query])

    def get_embeddings(self):
        return self.embeddings

    def get_papers(self):
        return self.papers