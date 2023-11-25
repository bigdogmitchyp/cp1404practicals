"""
CP1404 Prac
"""

from musician import Musician


class Band(Musician):
    """Band class"""

    def __init__(self, name=""):
        """Construct a Musician with a name and empty instrument collection."""
        super().__init__()
        self.name = name
        self.musicians = []

    def __str__(self):
        """Form a string to be printed when class is called"""
        return f"{self.name} ({','.join([str(musicians) for musicians in self.musicians])})"

    def play(self):
        """Lists musicians in band and the instruments they play"""
        return "\n".join([member.play() for member in self.musicians])

    def add(self, musicians):
        """Adds musicians to the band"""
        self.musicians.append(musicians)
