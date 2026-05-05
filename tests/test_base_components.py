import unittest
from src.scraper import BaseScraper
from src.parser import BaseParser
from src.storage import BaseStorage

class TestBaseScraper(unittest.TestCase):
    def test_init(self):
        scraper = BaseScraper()
        self.assertIsNotNone(scraper)

class TestBaseParser(unittest.TestCase):
    def test_init(self):
        parser = BaseParser("<html><body><h1>Test</h1></body></html>")
        self.assertIsNotNone(parser)

class TestBaseStorage(unittest.TestCase):
    def test_init(self):
        storage = BaseStorage()
        self.assertIsNotNone(storage)

if __name__ == '__main__':
    unittest.main()