from sklearn.metrics.pairwise import cosine_similarity
from search.transformer import PaperTransformer

class SearchEngine:

    def __init__(self):
        self.vectorizer = PaperTransformer()
        self.vectorizer.build_index()

    def search(self, query, top_k=10, year=None, category=None, mode="semantic"):

        embeddings = self.vectorizer.get_embeddings()
        papers = self.vectorizer.get_papers()

        # 🔹 AUTHOR SEARCH (NEW - added safely)
        if mode == "author":
            query_lower = query.lower()

            filtered_papers = [
                p for p in papers
                if query_lower in p.get("authors", "").lower()
            ]
            return filtered_papers[:top_k]

        query_vector = self.vectorizer.encode_query(query)

        similarity = cosine_similarity(query_vector, embeddings)[0]

        # Pair each paper with its similarity score
        scored_papers = list(zip(similarity, papers))

        # 🔥 Apply filters (NEW)
        if year:
            scored_papers = [p for p in scored_papers if p[1].get("year") == str(year)]

        if category:
            scored_papers = [p for p in scored_papers if p[1].get("category") == category]

        # Sort by similarity score (descending)
        scored_papers.sort(key=lambda x: x[0], reverse=True)

        # Get top results
        results = []
        for score, paper in scored_papers[:top_k]:
            paper_copy = paper.copy()
            paper_copy["score"] = float(score)
            results.append(paper_copy)

        return results