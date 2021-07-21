from bs4 import BeautifulSoup
import requests


class Soup:
    def __init__(self, iterable):
        self.iterable = iterable

    @staticmethod
    def get_url(domain, path):
        return f"{domain}" if id == 1 else path

    @staticmethod
    def get_lxml(domain, path):
        response = requests.get(Soup.get_url(domain, path))
        return BeautifulSoup(response.text, 'lxml')
