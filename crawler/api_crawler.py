import feedparser

def fetch_papers(category="cs.AI", max_results=100, start=0):
    url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&start={start}&max_results={max_results}"
    
    feed = feedparser.parse(url)

    papers = []

    for entry in feed.entries:
        # ✅ Convert everything to string (fixes Pylance issues)
        entry_id = str(entry.id)
        title = str(entry.title)
        abstract = str(entry.summary)
        published = str(entry.published)
        link = str(entry.link)

        # ✅ Extract authors safely
        authors = ", ".join(
            [str(a.name) if hasattr(a, "name") else str(a) for a in entry.authors]
        )

        # ✅ Extract year safely
        year = published.split("-")[0]

        paper = {
            "id": entry_id.split("/")[-1],   # unique ID
            "category": category,
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "year": year,
            "date": published,
            "url": link,
            "pdf_link": link.replace("/abs/", "/pdf/")
        }

        papers.append(paper)

    return papers


# 🔹 Optional: test run
if __name__ == "__main__":
    papers = fetch_papers()

    for p in papers[:3]:  # print first 3
        print("\nTitle:", p["title"])
        print("Year:", p["year"])
        print("Authors:", p["authors"])
        print("-" * 80)