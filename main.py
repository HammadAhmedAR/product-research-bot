from config.settings import OUTPUT_FILENAME, HEADLESS_BROWSER
from src.scraper import BaseScraper
from src.parser import BaseParser
from src.product_parser import ProductParser
from src.storage import BaseStorage
import sys
import os


def get_user_input(prompt, default_value=None):
    """Get user input with a fallback to default value"""
    try:
        user_input = input(prompt)
        return user_input if user_input else default_value
    except EOFError:
        # If we can't get input, return default value
        print(f"\nUsing default value: {default_value}" if default_value else "\nNo input available, using defaults")
        return default_value
    except Exception as e:
        # Handle any other input errors
        print(f"\nError getting input: {e}")
        return default_value


def get_save_directory():
    """Get directory from user input with validation"""
    try:
        save_dir = input("Enter directory to save files (or press Enter for current directory): ")
        if save_dir.strip() == "":
            return None  # Use current directory
        # Validate directory
        if not os.path.exists(save_dir):
            print(f"Directory {save_dir} doesn't exist. Creating it.")
            os.makedirs(save_dir, exist_ok=True)
        return save_dir
    except Exception as e:
        print(f"Error getting directory: {e}")
        return None


def main():
    # Get user input for product and URL
    product_name = get_user_input("Enter the product you want to search for: ", "laptop")
    target_url = get_user_input("Enter the URL to scrape (or press Enter for default): ", "https://books.toscrape.com/")
    save_directory = get_save_directory()
    
    # Use defaults if no input provided
    if not product_name:
        product_name = "laptop"
    if not target_url:
        target_url = "https://books.toscrape.com/"
    
    print(f"Product: {product_name}")
    print(f"URL: {target_url}")
    if save_directory:
        print(f"Save directory: {save_directory}")
    else:
        print("Save directory: Current directory")
    
    all_scraped_data = []

    scraper = BaseScraper()
    storage = BaseStorage()

    print(f"Scraping URL: {target_url}")
    # Try fetching with requests first, then fallback to Selenium if needed
    html = scraper.fetch_page(target_url)
    if not html:  # If requests failed, try with Selenium
        print(f"Requests failed for {target_url}, trying with Selenium...")
        html = scraper.fetch_with_selenium(target_url, headless=HEADLESS_BROWSER)

    if html:
        # Use the ProductParser for more detailed product information
        parser = ProductParser(html, product_name)
        try:
            # Parse product information
            product_data = parser.parse_product_info()
            all_scraped_data.append(product_data)
            print(f"Successfully parsed product data from {target_url}")
        except Exception as e:
            print(f"Error parsing data from {target_url}: {e}")
    else:
        print(f"Failed to fetch HTML for {target_url} even with Selenium.")

    if all_scraped_data:
        # Save in different formats
        storage.save(all_scraped_data, OUTPUT_FILENAME.replace(".json", ".json"), save_directory)
        storage.save_to_csv(all_scraped_data, OUTPUT_FILENAME.replace(".json", ".csv"), save_directory)
        storage.save_to_xlsx(all_scraped_data, OUTPUT_FILENAME.replace(".json", ".xlsx"), save_directory)
    else:
        print("No data was scraped.")


# Placeholder for a parse_title method in BaseParser if needed
def parse_title(self):
    title_tag = self.soup.find("title")
    return title_tag.string if title_tag else "No title found"

BaseParser.parse_title = parse_title # Dynamically add method to BaseParser

if __name__ == "__main__":
    main()