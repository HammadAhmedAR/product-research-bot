# Product Research Bot Workflow

## Overview

The Product Research Bot is a web scraping tool designed to extract product information from e-commerce websites for research purposes. The application uses a combination of requests and Selenium to fetch web pages, BeautifulSoup to parse HTML content, and supports multiple output formats (JSON, CSV, Excel).

## Workflow Architecture

### 1. Entry Point (main.py)
- Initializes the scraper, parser, and storage components
- Iterates through configured target URLs
- Attempts to fetch each page using requests first, with Selenium as a fallback for JavaScript-heavy sites
- Processes and stores scraped data in multiple formats

### 2. Scraping Process

#### Initial Request Attempt
- Uses the `requests` library to fetch HTML content
- Applies configurable User-Agent headers to avoid blocks
- Handles timeouts and HTTP errors gracefully

#### Selenium Fallback
- If the initial requests approach fails, the application falls back to using Selenium
- Particularly useful for dynamic websites that require JavaScript execution
- Uses headless Chrome browser by default for better performance

### 3. Data Processing

#### HTML Parsing
- Uses BeautifulSoup library for parsing HTML content
- Extracts relevant data based on CSS selectors defined in config/selectors.json
- The BaseParser class provides a foundation for site-specific parsing logic

#### Data Extraction
- Extracts product information such as names, prices, descriptions, etc.
- Handles data transformation and cleaning

### 4. Storage and Output

#### Multiple Format Support
- JSON (.json)
- CSV (.csv)
- Excel (.xlsx)

#### Data Persistence
- All scraped data is saved with the BaseStorage class
- Handles file operations and error management
- Provides both saving and loading capabilities

## Component Interaction Flow

1. **Configuration**: The application starts by reading settings from `config/settings.py` which defines target URLs and output preferences.

2. **Scraping**: The `BaseScraper` attempts to fetch content using `requests` first, then falls back to Selenium.

3. **Parsing**: The `BaseParser` processes the HTML content and extracts relevant data.

4. **Storage**: The `BaseStorage` class handles saving the extracted data in multiple formats.

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

### Configuration Files
- `config/settings.py`: Application settings including target URLs and output preferences
- `config/selectors.json`: CSS selectors for data extraction

## Usage Workflow
1. Configure target URLs in `config/settings.py`
2. Run `python main.py`
3. The application will iterate through all configured URLs
4. Data is saved in the configured output formats