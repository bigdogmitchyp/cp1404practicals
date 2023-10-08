"""
CP1404 Practical
"""
import random


def main():
    """Print quick picks"""
    number_of_picks = get_pick_number()
    for i in range(number_of_picks):
        random_number_row = []
        generate_random_picks(random_number_row)
        random_number_row.sort()
        print(" ".join(f"{number:2}" for number in random_number_row))


def generate_random_picks(random_number_row):
    """Generate random number lists"""
    for j in range(6):
        number = random.randint(1, 45)
        number = check_if_number_valid(number, random_number_row)
        random_number_row.append(number)


def check_if_number_valid(number, random_number_row):
    """Makes sure the number lists are without replacement"""
    while number in random_number_row:
        number = random.randint(1, 45)
    return number


def get_pick_number():
    """Collect users number of picks"""
    number_of_picks = int(input("How many quick picks?: "))
    return number_of_picks


main()
