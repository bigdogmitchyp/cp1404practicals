"""
CP1404 prac
est 15 min
actual 7 min
"""

from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(f"{my_taxi} ${my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.add_fuel(75)
my_taxi.drive(100)
print(f"{my_taxi} ${my_taxi.get_fare()}")
