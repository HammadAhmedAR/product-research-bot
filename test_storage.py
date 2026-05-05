import os

# Test the storage functionality with a specific directory
from src.storage import BaseStorage

# Create test data
test_data = [
    {
        "product": "laptop",
        "url": "https://books.toscrape.com/",
        "title": "Test Product Data"
    }
]

# Create storage instance
storage = BaseStorage()

# Test saving to a specific directory
storage.save(test_data, "test_data.json", "test_output")
storage.save_to_csv(test_data, "test_data.csv", "test_output")
storage.save_to_xlsx(test_data, "test_data.xlsx", "test_output")

print("Test files saved to test_output directory")