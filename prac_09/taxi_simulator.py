"""
CP1404 Prac
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hoose taxi, d)rive"

print("Lets drive!")
print(MENU)


def main():
    """Taxi simulator"""
    current_taxi = None
    bill_to_date = 0
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "C":
            current_taxi = choose_taxi()
        elif user_choice == "D":
            if current_taxi:
                bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        user_choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    print_taxi_list()


def print_taxi_list():
    """Prints list of taxis"""
    running_count = 0
    for taxi in TAXIS:
        print(f"{running_count} - {taxi}")
        running_count += 1


def drive_taxi(taxi):
    """Drives current taxi for input distance"""
    if taxi:
        try:
            trip_distance = int(input("Drive how far? "))
            taxi.drive(trip_distance)
            print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")
            return taxi.get_fare()
        except ValueError:
            print("Invalid number")
    else:
        print("you need to choose a taxi before you can drive")


def choose_taxi():
    """Select taxi from list of taxis"""
    print("Taxis available:")
    print_taxi_list()
    try:
        current_taxi = int(input("Choose taxi: "))
        return TAXIS[current_taxi]
    except ValueError:
        print("Invalid number")
    except IndexError:
        print("Invalid taxi choice")


main()
