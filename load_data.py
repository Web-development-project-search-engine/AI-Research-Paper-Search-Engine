from preprocessing.clean_text import clean_text
from database.db import insert_papers
from sentence_transformers import SentenceTransformer
from crawler.api_crawler import fetch_papers

model = SentenceTransformer('all-MiniLM-L6-v2')

papers = fetch_papers()

if not papers:
    print("No papers fetched from API")
    exit()

for paper in papers:

    title = clean_text(paper.get("title", ""))
    abstract = clean_text(paper.get("abstract", ""))
    authors = clean_text(paper.get("authors", ""))

    combined_text = f"{title} {abstract} {authors}"

    # 🔥 IMPORTANT FIX: force list output for consistency
    embedding = model.encode([combined_text])[0]

    paper["cleaned_title"] = title
    paper["cleaned_abstract"] = abstract
    paper["cleaned_authors"] = authors

    paper["embedding"] = embedding.tolist()

insert_papers(papers)

print("All papers stored in MongoDB successfully!")