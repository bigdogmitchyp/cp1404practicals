"""
CP1404 prac module
est time = 14 min
start time = 1314
end time = 1320
total time = 6 min
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def __iter__(self):
        return [self.name, self.year, float(self.cost)]

    def get_age(self):
        guitar_age = 2023 - self.year
        return guitar_age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
