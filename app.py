from flask import Flask, render_template, request
from search.search_engine import search_papers
import json

app = Flask(__name__)

# Load papers for paper detail page
with open("papers.json", "r", encoding="utf-8") as f:
    papers_data = json.load(f)

# Home Page

@app.route("/")
def home():
    return render_template("index.html")


# Search Route
@app.route("/search")
def search():
    query = request.args.get("q")

    if not query:
        return render_template("results.html", results=[], query="")
    
    results = search_papers(query)
    return render_template("results.html", results=results, query=query)


# Paper Detail Page
@app.route("/paper/<int:paper_id>")
def paper_detail(paper_id):
    if paper_id < 0 or paper_id >= len(papers_data):
        return "Paper not found", 404
    
    paper = papers_data[paper_id]
    return render_template("paper.html", paper=paper)


# Run App
if __name__ == "__main__":
    app.run(debug=True)