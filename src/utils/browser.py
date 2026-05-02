
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--log-level=3') # Suppress console logs
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            print("Browser initialized successfully.")
        except Exception as e:
            print(f"Error initializing browser: {e}")
            self.driver = None

    def get_page(self, url):
        if not self.driver:
            print("Browser not initialized.")
            return None
        try:
            self.driver.get(url)
            print(f"Navigated to {url}")
            return self.driver.page_source
        except Exception as e:
            print(f"Error navigating to {url}: {e}")
            return None

    def close(self):
        if self.driver:
            self.driver.quit()
            print("Browser closed.")
