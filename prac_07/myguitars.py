"""
CP1404 Practical module
"""

import csv
from guitar import Guitar


def main():
    """Guitar list program"""
    guitars = get_guitars()
    print_guitars(guitars)
    get_new_guitar_from_user(guitars)
    print_guitars(guitars)
    save_guitars_to_csv(guitars)


def save_guitars_to_csv(guitars):
    """Saves changes made to list to csv file"""
    with open("guitars.csv", 'w', encoding="utf-8") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def get_new_guitar_from_user(guitars):
    """Takes user input for adding new guitars to list"""
    guitar_name = input("New guitar: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = input("Price: ")
        guitar = Guitar(guitar_name, int(guitar_year), float(guitar_cost))
        guitars.append(guitar)
        guitars.sort()
        guitar_name = input("New guitar: ")


def print_guitars(guitars):
    """Prints guitar info with formatting"""
    for guitar in guitars:
        print(f"{guitar.name} ({guitar.year}) : {guitar.cost:,.2f}")


def get_guitars():
    """Loads guitar info from a csv file"""
    with open('guitars.csv', 'r', newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        guitars = []
        for row in reader:
            guitar = Guitar((row[0]), int(row[1]), float(row[2]))
            guitars.append(guitar)
        guitars.sort()
        return guitars


main()
