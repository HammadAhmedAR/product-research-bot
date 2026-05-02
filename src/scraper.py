import requests

class BaseScraper:
    def __init__(self, user_agent=None):
        self.user_agent = user_agent
        self.headers = {"User-Agent": self.user_agent or "Mozilla/5.0"}

    def fetch_page(self, url):
        """
        Fetch the HTML content of a given URL.
        Uses a configurable User-Agent to avoid blocks.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            print(f"Page fetched successfully: {url}")
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch page {url}: {e}")
            return None

    def fetch_with_selenium(self, url, headless=True):
        """
        Fetch the HTML content of a given URL using Selenium.
        Useful for dynamic websites that require JavaScript execution.
        """
        from src.utils.browser import Browser
        browser = Browser(headless=headless)
        html = browser.get_page(url)
        browser.close()
        return html
