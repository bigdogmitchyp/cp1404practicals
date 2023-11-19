"""
CP1404 Prac
"""
from car import Car
import random


class UnreliableCar(Car):
    """Class for a car which has a chance of failing to drive"""
    def __init__(self, name, fuel, reliability):
        """Initialises an unreliable car instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Calculates how far car drives"""
        if random.uniform(0, 100) < self.reliability:
            distance = 0
        elif distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
