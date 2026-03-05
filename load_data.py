import json

from preprocessing.clean_text import clean_text

from database.db import insert_papers

with open("papers.json", "r", encoding="utf-8") as f:
    papers = json.load(f)

for paper in papers:

    paper["cleaned_title"] = clean_text(paper["title"])

    paper["cleaned_abstract"] = clean_text(paper["abstract"])


insert_papers(papers)

print("All cleaned papers stored in MongoDB successfully!")