"""
CP1404 prac module
start time = 1237
end time = 1300
total time = 23
I forgot to guess time oops
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="static", reflection="False", year="1991"):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.reflection == 1:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection={self.is_dynamic()}, First appeared in {self.year}"
