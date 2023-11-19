"""
CP1404 Prac
"""

from taxi import Taxi

flagfall = 4.50


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a fancy taxi service"""
        super().__init__(name, fuel, )
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance} plus flagfall of $4.50"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + flagfall
