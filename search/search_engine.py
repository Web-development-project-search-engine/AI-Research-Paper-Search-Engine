from .vectorizer import build_vectorizer
from .similarity import compute_similarity

# Build when the app starts
vectorizer, tfidf_matrix, papers = build_vectorizer()

def search_papers(query, top_k=5):
    scores = compute_similarity(query, vectorizer, tfidf_matrix)

    ranked_indices = scores.argsort()[::-1][:top_k]

    results = []
    for idx in ranked_indices:
        results.append({
            "title": papers[idx]["title"],
            "abstract": papers[idx]["abstract"],
            "score": float(scores[idx])
        })

    return results