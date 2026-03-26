from sklearn.feature_extraction.text import TfidfVectorizer
from database.db import get_all_papers

class PaperVectorizer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = None
        self.papers = []

    def build_index(self):
        # load papers from mongodb
        self.papers = get_all_papers()

        documents = []

        for paper in self.papers:
            text = paper["cleaned_title"] + " " + paper["cleaned_abstract"]+""+paper["cleaned_authors"]
            documents.append(text)

        # build tfidf matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(documents)

        print("TF-IDF index built successfully")

    def get_matrix(self):
        return self.tfidf_matrix

    def get_vectorizer(self):
        return self.vectorizer

    def get_papers(self):
        return self.papers