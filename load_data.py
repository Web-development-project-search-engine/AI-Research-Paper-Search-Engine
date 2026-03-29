from preprocessing.clean_text import clean_text
from database.db import insert_papers
from sentence_transformers import SentenceTransformer
from crawler.api_crawler import fetch_papers

model = SentenceTransformer('all-MiniLM-L6-v2')

papers = fetch_papers()   # ✅ API instead of JSON

for paper in papers:

    paper["cleaned_title"] = clean_text(paper["title"])
    paper["cleaned_abstract"] = clean_text(paper["abstract"])
    paper["cleaned_authors"] = clean_text(paper.get("authors", ""))

    combined_text = (
        paper["cleaned_title"] * 3 + " " +
        paper["cleaned_abstract"] + " " +
        paper["cleaned_authors"]
    )

    embedding = model.encode(combined_text)
    paper["embedding"] = embedding.tolist()

insert_papers(papers)

print("All papers stored in MongoDB successfully!")