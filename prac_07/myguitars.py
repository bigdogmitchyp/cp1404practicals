"""
CP1404 Practical module
"""

import csv
from guitar import Guitar
from operator import itemgetter


def main():
    in_file = open('guitars.csv', 'r', newline='')
    reader = csv.reader(in_file)
    guitars = []
    for row in reader:
        guitar = Guitar((row[0]), int(row[1]), float(row[2]))
        guitar = guitar.create_list()
        guitars.append(guitar)
    sorted_guitars = (sorted(guitars, key=itemgetter(1)))
    for guitar in sorted_guitars:
        print(f"{guitar[0]} ({guitar[1]}) : {guitar[2]:,.2f}")
    guitar_name = input("New guitar: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = input("Price: ")
        guitar = Guitar(guitar_name, int(guitar_year), float(guitar_cost))
        guitar = guitar.create_list()
        guitars.append(guitar)
        sorted_guitars = (sorted(guitars, key=itemgetter(1)))
        for guitar in sorted_guitars:
            print(f"{guitar[0]} ({guitar[1]}) : {guitar[2]:,.2f}")
        guitar_name = input("New guitar: ")
    with open("guitars.csv", 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(guitars)
    in_file.close()


main()
