# Product Research Bot

A web scraping tool designed to extract product information from e-commerce websites for research purposes.

## Features

- Fetches web pages using both requests and Selenium
- Parses HTML content with BeautifulSoup
- Supports multiple output formats (JSON, CSV, Excel)
- Configurable user agents and browser settings
- Headless browser support for JavaScript-heavy sites
- Interactive user prompts for product, URL, and save location input

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install ChromeDriver (required for Selenium):
   The application uses webdriver-manager to automatically manage ChromeDriver.

## Configuration

Edit `config/settings.py` to customize:
- OUTPUT_FILENAME: Default output filename
- USER_AGENT: Browser user agent string
- HEADLESS_BROWSER: Whether to run browser in headless mode

## Usage

Run the scraper:
```
python main.py
```

When you run the script, you'll be prompted to enter:
1. The product you want to search for
2. The URL to scrape (or press Enter for default)
3. The directory where you want to save the files (or press Enter for current directory)

## Project Structure

```
product-research-bot/
├── config/
│   ├── settings.py
│   └── selectors.json
├── src/
│   ├── scraper.py
│   ├── parser.py
│   ├── product_parser.py
│   ├── storage.py
│   └── utils/
│       ├── browser.py
│       ├── logger.py
│       └── helpers.py
├── main.py
├── requirements.txt
├── WORKFLOW.md
└── README.md
```

## Output Formats

The scraper can save data in multiple formats:
- JSON (.json)
- CSV (.csv)
- Excel (.xlsx)

## Legal Notice

This tool is for educational and research purposes only. Please ensure you comply with the website's terms of service and robots.txt before scraping. Respect rate limits and avoid overloading servers.