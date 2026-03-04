# This file load papers, build TF-IDF matrix and return vectorizer+matrix

import json
from sklearn.feature_extraction.text import TfidfVectorizer

def build_vectorizer(json_path="papers.json"):
    # Loading the papers in papers.json
    with open(json_path, "r", encoding="utf-8") as f:
        papers = json.load(f)

    # Combine both title and abstract
    documents = []
    for paper in papers:
        text = paper["title"]+" "+paper["abstract"]
        documents.append(text)

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    return vectorizer, tfidf_matrix, papers


