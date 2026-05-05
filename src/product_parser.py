from src.parser import BaseParser
from bs4 import BeautifulSoup
import json
import re


class ProductParser(BaseParser):
    def __init__(self, html, product_name=None):
        super().__init__(html)
        self.product_name = product_name
        self.product_selectors = self._load_selectors()
        
    def _load_selectors(self):
        """Load selectors from the config file for product parsing"""
        # Default selectors for common e-commerce sites
        return {
            "product_name": [
                "[class*='title']",
                "[class*='product'] [class*='name']",
                "[class*='product'] h1",
                "h1",
                "h2"
            ],
            "price": [
                "[class*='price']",
                "[class*='cost']",
                "[class*='amount']"
            ],
            "description": [
                "[class*='description']",
                "[class*='desc']",
                "[class*='details'] p"
            ],
            "image": [
                "img[class*='product']",
                "img[class*='image']",
                "img"
            ]
        }
    
    def parse_product_info(self):
        """Parse product information from the HTML"""
        product_info = {
            "product_name": self.product_name or "Unknown Product",
            "url": "Unknown URL",
            "title": self.parse_title(),
            "price": self._extract_price(),
            "description": self._extract_description(),
            "images": self._extract_images(),
            "metadata": self._extract_metadata()
        }
        return product_info
    
    def _extract_price(self):
        """Extract price information"""
        for selector in self.product_selectors["price"]:
            elements = self.soup.select(selector)
            for element in elements:
                # Try to extract text that looks like a price
                text = element.get_text().strip()
                if text and (text.startswith('$') or re.search(r'\d+\.?\d*', text)):
                    return text
                elif element.get('content'):  # For meta tags
                    return element.get('content')
        return "Price not found"
    
    def _extract_description(self):
        """Extract product description"""
        for selector in self.product_selectors["description"]:
            elements = self.soup.select(selector)
            for element in elements:
                text = element.get_text().strip()
                if text and len(text) > 20:  # Likely a real description
                    return text
        return "Description not found"
    
    def _extract_images(self):
        """Extract product images"""
        images = []
        for selector in self.product_selectors["image"]:
            elements = self.soup.select(selector)
            for element in elements:
                if element.name == 'img':
                    src = element.get('src') or element.get('data-src') or element.get('data-lazy-src')
                    if src:
                        images.append(src)
        return images[:5]  # Return up to 5 images
    
    def _extract_metadata(self):
        """Extract additional metadata"""
        metadata = {}
        # Extract all meta tags
        meta_tags = self.soup.find_all('meta')
        for tag in meta_tags:
            if tag.get('name') and tag.get('content'):
                metadata[tag.get('name')] = tag.get('content')
            elif tag.get('property') and tag.get('content'):
                metadata[tag.get('property')] = tag.get('content')
        return metadata