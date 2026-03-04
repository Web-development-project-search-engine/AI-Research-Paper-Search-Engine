from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(query, vectorizer, tfidf_matrix):
    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    return similarity_scores[0]