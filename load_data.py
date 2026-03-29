import json
from preprocessing.clean_text import clean_text
from database.db import insert_papers
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
with open("papers.json", "r", encoding="utf-8") as f:
    papers = json.load(f)

for paper in papers:

    paper["cleaned_title"] = clean_text(paper["title"])
    paper["cleaned_abstract"] = clean_text(paper["abstract"])
    paper["cleaned_authors"] = clean_text(paper.get("authors", ""))

    combined_text = (
        paper["cleaned_title"] * 3 + " " +
        paper["cleaned_abstract"] + " " +
        paper["cleaned_authors"]
    )

    # Generate Embeddings
    embedding = model.encode(combined_text)

    # Store embeddings in DB (Converting into list)
    paper["embedding"] = embedding.tolist()

insert_papers(papers)

print("All cleaned papers stored in MongoDB successfully!")