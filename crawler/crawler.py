import requests
from bs4 import BeautifulSoup
import time
import json

BASE_URL = "https://arxiv.org"

CATEGORIES = [
    "cs.AI","cs.AR","cs.CC","cs.CE","cs.CG","cs.CL","cs.CR","cs.CV",
    "cs.CY","cs.DB","cs.DC","cs.DL","cs.DM","cs.DS","cs.ET","cs.FL",
    "cs.GL","cs.GR","cs.GT","cs.HC","cs.IR","cs.IT","cs.LG","cs.LO",
    "cs.MA","cs.MM","cs.MS","cs.NA","cs.NE","cs.NI","cs.OH","cs.OS",
    "cs.PF","cs.PL","cs.RO","cs.SC","cs.SD","cs.SE","cs.SI","cs.SY"
]

all_papers = []

PAGES_PER_CATEGORY = 1
PAPERS_PER_PAGE = 5

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_listing_page(category, skip):
    url = f"{BASE_URL}/list/{category}/recent?skip={skip}&show=25"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch {category}")
        return None
    
    return response.text

def extract_paper_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", title="Abstract")

    paper_links = []
    for link in links:
        href = link.get("href")
        if href:
            paper_links.append(BASE_URL + href)

    return paper_links

def extract_paper_details(url, category):
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to fetch paper")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("h1", class_="title")
    title = title_tag.text.replace("Title:", "").strip() if title_tag else "N/A"

    abstract_tag = soup.find("blockquote", class_="abstract")
    abstract = abstract_tag.text.replace("Abstract:", "").strip() if abstract_tag else "N/A"

    authors_tag = soup.find("div", class_="authors")
    authors = authors_tag.text.replace("Authors:", "").strip() if authors_tag else "N/A"

    subjects_tag = soup.find("div", class_="subheader")
    subjects = subjects_tag.text.replace("Subjects:", "").strip() if subjects_tag else "N/A"

    pdf_tag = soup.find("a", href=lambda x: x and x.startswith("/pdf/"))
    pdf_link = BASE_URL + pdf_tag["href"] if pdf_tag else "N/A"

    paper_data = {
        "category": category,
        "title": title,
        "abstract": abstract,
        "authors": authors,
        "subjects": subjects,
        "url": url,
        "pdf_link": pdf_link
    }

    return paper_data

def crawl():
    print("Strating crawler...\n")

    for category in CATEGORIES:
        print(f"\nCrawling Category: {category}")
        
        for page in range(PAGES_PER_CATEGORY):
            skip = page*25

            listing_html = get_listing_page(category, skip)

            if not listing_html:
                continue
                
            paper_links = extract_paper_links(listing_html)

            for link in paper_links[:PAPERS_PER_PAGE]:
                print("\nVisiting: ", link)
                paper = extract_paper_details(link, category)

                if paper:
                    all_papers.append(paper)
                    print("Saved: ", paper["title"])
                time.sleep(2)

    # Save to JSON
    with open("papers.json", "w", encoding="utf-8") as f:
        json.dump(all_papers, f, indent=4, ensure_ascii=False)

    print(f"\nSaved {len(all_papers)} papers to papers.json")
    print("\nCrawling completed.")


if __name__=="__main__":
    crawl()