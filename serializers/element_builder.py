class Iterable:
  def __init__(self, iterable):
    self.name = iterable

  def build(self, lxml):
    return lxml.find_all('table', class_="schedule")