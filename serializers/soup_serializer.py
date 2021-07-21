from classes.soup import Soup

class SoupSerializer:
    def __init__(self, soup=Soup()):
        self.soup = soup

    def build(self):
        return self.soup

    @property
    def game(self):
        GameBuilder(self.soup)

class GameBuilder:
    def __init__(self, soup):
        super().__init__(soup)

    def opponent(self, away_team):
        self.soup.away_team = away_team
        return self

    def team(self, home_team):
        self.soup.home_team = home_team
        return self

    def at(self, date_time):
        self.soup.date_time = date_time
        return self

    def location(self, location):
        self.soup.location = location
        return self

    def stadium(self, stadium):
        self.soup.stadium = stadium
        return self

class ScheduleBuilder:
    def __init__(self, soup):
        super().__init__(soup)

    def

    