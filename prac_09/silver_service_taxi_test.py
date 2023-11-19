"""
CP1404 Prac
"""

from silver_service_taxi import SilverServiceTaxi


my_taxi = SilverServiceTaxi("Tesla", 1000, 2)
my_taxi.drive(18)
print(my_taxi)
print(f"${my_taxi.get_fare()}")
