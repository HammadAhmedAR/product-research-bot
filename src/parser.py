
from bs4 import BeautifulSoup

class BaseParser:
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, "html.parser")

    def parse(self):
        # This method should be implemented by subclasses
        raise NotImplementedError
