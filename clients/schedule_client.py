import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from serializers.schedule_serializer import ScheduleSerializer


class ScheduleClient:
    def __init__(self, path=None):
        self.domain = f'https://www.espn.com/nfl/schedule/'
        self.path = path
        self.schedule = []

    def get_schedule(self):
        response = requests.get(self.get_url())
        soup = BeautifulSoup(response.text, 'lxml')
        self.parse_soup(soup)

    def get_url(self):
        return f"{self.domain}/{self.path}" if self.path else self.domain

    def parse_soup(self, soup):
        tables = soup.find_all('table', class_="schedule")
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                row_items = []
                items = row.find_all('td')
                for item in items:
                    date = item.get('data-date')
                    if 'tickets' in item.get('class', {}) or 'network' in item.get('class', {}):
                        continue
                    else:
                        if len(item.text):
                            row_items.append(item.text)
                        if date:
                            row_items.append(date)
                if len(row_items):
                    self.schedule.append(row_items)
