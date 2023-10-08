"""
CP1404 Practical
"""
import random


def main():
    number_of_picks = int(input("How many quick picks?: "))
    for i in range(number_of_picks):
        random_number_row = []
        for j in range(6):
            number = random.randint(1, 45)
            while number in random_number_row:
                number = random.randint(1, 45)
            random_number_row.append(number)
        random_number_row.sort()
        print(" ".join(f"{number:2}" for number in random_number_row))


main()
