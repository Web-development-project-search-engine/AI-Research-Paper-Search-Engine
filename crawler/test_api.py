from crawler.api_crawler import fetch_papers

def test_fetch():
    papers = fetch_papers("cs.AI", max_results=5)

    print("\nFetched Papers:\n")

    for i, paper in enumerate(papers, 1):
        print(f"{i}. {paper['title']}")
        print("Authors:", paper["authors"])
        print("Year:", paper["year"])
        print("Link:", paper["url"])
        print("-" * 80)

if __name__ == "__main__":
    test_fetch()