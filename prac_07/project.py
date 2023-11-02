"""
CP1404 practical module
"""


class Project:

    def __init__(self, name="", date="", prio=0, cost=0.0, completion=0):
        self.name = name
        self.date = date
        self.priority = prio
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return f"{self.name}, {self.date}, {self.priority}, {self.cost}, {self.completion}"

    def __repr__(self):
        return f"{self.name}, {self.date}, {self.priority}, {self.cost}, {self.completion}"
