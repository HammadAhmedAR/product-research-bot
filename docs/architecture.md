# Project Documentation

## Architecture Overview

The product research bot follows a modular architecture with the following components:

1. **Scraper** - Handles fetching web page content using requests or Selenium
2. **Parser** - Parses HTML content using BeautifulSoup
3. **Storage** - Saves data in various formats (JSON, CSV, Excel)
4. **Configuration** - Centralized configuration management
5. **Utilities** - Helper functions and browser management

## Component Details

### Scraper (`src/scraper.py`)
- `BaseScraper`: Main class for fetching web pages
- `fetch_page()`: Uses requests for simple pages
- `fetch_with_selenium()`: Uses Selenium for JavaScript-heavy pages

### Parser (`src/parser.py`)
- `BaseParser`: Base class for parsing HTML content
- Uses BeautifulSoup for HTML parsing
- Designed for extension with site-specific parsers

### Storage (`src/storage.py`)
- `BaseStorage`: Handles data persistence
- Supports JSON, CSV, and Excel formats
- Includes error handling for file operations

### Configuration (`config/settings.py`)
- Centralized configuration settings
- URL lists, output settings, browser options
- User agent customization

## Data Flow

1. Main script initializes components
2. URLs are processed one by one
3. Scraper fetches HTML content
4. Parser extracts relevant data
5. Storage saves data to files

## Extending the Bot

To add support for specific websites:
1. Create a subclass of `BaseParser`
2. Implement site-specific parsing logic
3. Update the main script to use your parser