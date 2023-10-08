"""
CP1404 Practical
"""
import random


def main():
    number_of_picks = int(input("How many quick picks?: "))
    for i in range(number_of_picks):
        list_of_numbers = [random.sample(range(1, 46), 6)]
        string_of_numbers = str(list_of_numbers).replace(", ", " ").strip("[]")
        print(string_of_numbers)


main()
