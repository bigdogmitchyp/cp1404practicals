"""
CP1404 Practical module
"""

import csv
from guitar import Guitar


def main():
    in_file = open('guitars.csv', 'r', newline='')
    reader = csv.reader(in_file)
    guitars = []
    for row in reader:
        guitar = Guitar(row[0], row[1], float(row[2]))
        guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    guitar_name = input("New guitar: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = input("Price: ")
        guitar = Guitar(guitar_name, guitar_year, float(guitar_cost))
        guitars.append(guitar)
        for guitar in guitars:
            print(guitar)
        guitar_name = input("New guitar: ")
    in_file.close()


main()
