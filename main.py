from config.settings import TARGET_URLS, OUTPUT_FILENAME, HEADLESS_BROWSER
from src.scraper import BaseScraper
from src.parser import BaseParser
from src.storage import BaseStorage


def main():
    all_scraped_data = []

    scraper = BaseScraper()
    storage = BaseStorage()

    for url in TARGET_URLS:
        print(f"Scraping URL: {url}")
        # Try fetching with requests first, then fallback to Selenium if needed
        html = scraper.fetch_page(url)
        if not html:  # If requests failed, try with Selenium
            print(f"Requests failed for {url}, trying with Selenium...")
            html = scraper.fetch_with_selenium(url, headless=HEADLESS_BROWSER)

        if html:
            # Example: If you have a specific parser for this site, use it
            # For now, we use a generic parser that might need to be subclassed
            parser = BaseParser(html)
            # In a real scenario, you would have specific parsing logic here
            # Example: parsed_data = parser.parse_books()
            # For demonstration, let's just count the tags
            try:
                # This is a placeholder for actual parsing logic
                # A real implementation would extract specific data like product names, prices, etc.
                data_from_page = {
                    "url": url,
                    "content_length": len(html),
                    "title": parser.parse_title() if hasattr(parser, "parse_title") else "N/A"
                }
                all_scraped_data.append(data_from_page)
                print(f"Successfully parsed data from {url}")
            except Exception as e:
                print(f"Error parsing data from {url}: {e}")
        else:
            print(f"Failed to fetch HTML for {url} even with Selenium.")

    if all_scraped_data:
        # Save in different formats
        storage.save(all_scraped_data, OUTPUT_FILENAME.replace(".json", ".json"))
        storage.save_to_csv(all_scraped_data, OUTPUT_FILENAME.replace(".json", ".csv"))
        storage.save_to_xlsx(all_scraped_data, OUTPUT_FILENAME.replace(".json", ".xlsx"))
    else:
        print("No data was scraped.")

# Placeholder for a parse_title method in BaseParser if needed
def parse_title(self):
    title_tag = self.soup.find("title")
    return title_tag.string if title_tag else "No title found"

BaseParser.parse_title = parse_title # Dynamically add method to BaseParser

if __name__ == "__main__":
    main()
