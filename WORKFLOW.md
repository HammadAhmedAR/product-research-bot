# Product Research Bot Workflow

## Overview

The Product Research Bot is a web scraping tool designed to extract product information from e-commerce websites for research purposes. The application uses a combination of requests and Selenium to fetch web pages, BeautifulSoup to parse HTML content, and supports multiple output formats (JSON, CSV, Excel).

## Workflow Architecture

### 1. Entry Point (main.py)
- Initializes the scraper, parser, and storage components
- Prompts user for product name, target URL, and save location
- Attempts to fetch each page using requests first, with Selenium as a fallback for JavaScript-heavy sites
- Processes and stores scraped data in multiple formats

### 2. User Input Process

#### Interactive Prompts
When the script is run, it will prompt the user for:
1. Product name to search for
2. Target URL to scrape
3. Directory to save the output files

### 3. Scraping Process

#### Initial Request Attempt
- Uses the `requests` library to fetch HTML content
- Applies configurable User-Agent headers to avoid blocks
- Handles timeouts and HTTP errors gracefully

#### Selenium Fallback
- If the initial requests approach fails, the application falls back to using Selenium
- Particularly useful for dynamic websites that require JavaScript execution
- Uses headless Chrome browser by default for better performance

### 4. Data Processing

#### HTML Parsing
- Uses BeautifulSoup library for parsing HTML content
- Extracts relevant product data using the ProductParser class
- Handles data transformation and cleaning

### 5. Storage and Output

#### Multiple Format Support
- JSON (.json)
- CSV (.csv)
- Excel (.xlsx)

#### Custom Save Locations
- Users can specify a custom directory to save the output files
- If the directory doesn't exist, it will be created automatically
- All scraped data is saved with the BaseStorage class

## Component Interaction Flow

1. **User Input**: The application starts by asking the user for a product name, URL, and save location.

2. **Scraping**: The `BaseScraper` attempts to fetch content using `requests` first, then falls back to Selenium.

3. **Parsing**: The `ProductParser` processes the HTML content and extracts relevant product data.

4. **Storage**: The `BaseStorage` class handles saving the extracted data in multiple formats to the user-specified location.

## Technical Details

### Dependencies
- `requests`: For simple HTTP requests
- `beautifulsoup4`: For HTML parsing
- `selenium`: For JavaScript-heavy sites
- `webdriver-manager`: For automatic ChromeDriver management
- `pandas`: For data manipulation and storage in various formats
- `openpyxl`: For Excel file support

### Error Handling
- Network errors are caught and logged
- Fallback mechanisms ensure robust scraping
- Data validation and cleaning before storage
- Directory creation if needed

### Configuration Files
- `config/settings.py`: Application settings including output preferences
- `config/selectors.json`: CSS selectors for data extraction (currently not used but available for future enhancements)

## Usage Workflow
1. Run `python main.py`
2. Enter the product name when prompted
3. Enter the URL when prompted (or press Enter for default)
4. Enter the directory where you want to save the files (or press Enter for current directory)
5. The application will scrape the specified URL for the product
6. Data is saved in the specified directory in the configured output formats