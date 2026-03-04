import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://arxiv.org"
CATEGORY = "cs.AI"

PAGES_TO_CRAWL = 2
PAPERS_PER_PAGE = 5

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_listing_page(skip):
    url = f"{BASE_URL}/list/{CATEGORY}/recent?skip={skip}&show=25"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch listing page")
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

def extract_paper_details(url):
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to fetch paper")
        return
    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("h1", class_="title")
    title = title_tag.text.replace("Title:", "").strip() if title_tag else "N/A"

    abstract_tag = soup.find("blockquote", class_="abstract")
    abstract = abstract_tag.text.replace("Abstract:", "").strip() if abstract_tag else "N/A"

    print("TITLE: ", title)
    print("ABSTRACT: ", abstract[:250], "...")
    print("-"*80)

def crawl():
    print("Strating crawler...\n")

    for page in range(PAGES_TO_CRAWL):
        skip = page*25
        print(f"\nFething Page {page+1} (skip={skip})")

        listing_html = get_listing_page(skip)

        if not listing_html:
            continue
            
        paper_links = extract_paper_links(listing_html)

        print(f"Found {len(paper_links)} papers")

        for link in paper_links[:PAPERS_PER_PAGE]:
            print("\nVisiting: ", link)
            extract_paper_details(link)
            time.sleep(2)

    print("\nCrawling completed.")


if __name__=="__main__":
    crawl()