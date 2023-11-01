"""
CP1404 prac module
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, {self.year}, {self.cost}"

    def __iter__(self):
        return self

    def __repr__(self):
        return f"{self.name}, {self.year}, {self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        guitar_age = 2023 - self.year
        return guitar_age

    def is_vintage(self):
        return self.get_age() >= 50

    def create_list(self):
        return [self.name, self.year, self.cost]
