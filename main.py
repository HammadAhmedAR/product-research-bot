from scraper.base_scraper import BaseScraper

def main():
    url = "https://books.toscrape.com/"

    scraper = BaseScraper()
    html = scraper.fetch_page(url)

    if html:
        print("HTML fetched. Length:", len(html))
    else:
        print("Failed to fetch HTML")

if __name__ == "__main__":
    main()