import requests
from bs4 import BeautifulSoup
from serializers.schedule_serializer import ScheduleSerializer


class ScheduleClient:
    def __init__(self, id):
        self.domain = f'https://www.espn.com/nfl/schedule'
        self.schedule = []
        self.id = id

    def get_schedule(self):
        response = requests.get(self.get_url())
        soup = BeautifulSoup(response.text, 'lxml')
        self.parse_soup(soup)

    def get_url(self):
        return f"{self.domain}" if self.id == 1 else f"{self.domain}/_/week/{self.id}"

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
