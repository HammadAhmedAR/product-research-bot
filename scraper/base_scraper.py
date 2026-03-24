import requests

class BaseScraper:
    def fetch_page(self, url):
        """
        Fetch the HTML content of a given URL.
        Uses a fake browser User-Agent to avoid blocks.
        """
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("Page fetched successfully!")
            return response.text
        else:
            print("Failed to fetch page:", response.status_code)
            return None