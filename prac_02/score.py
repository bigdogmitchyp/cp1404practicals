"""
CP1404 Week 2 Prac
"""
import random


def main():
    """This function will covert scores into grades"""
    score = collect_user_score()
    return_grade(score)
    random_score = return_random_score()
    return_grade(random_score)


def return_random_score():
    """This function generates a random score"""
    random_score = random.randint(0, 100)
    return random_score


def return_grade(score):
    """This function will assign a grade to a score"""
    if score > 100 or score < 0:
        print_invalid()
    elif score >= 90:
        print_excellent()
    elif score >= 50:
        print_passable()
    else:
        print_bad()


def print_bad():
    """This function will print a bad grade"""
    print("Bad")


def print_passable():
    """This function will print a passable grade"""
    print("Passable")


def print_excellent():
    """This function will print an excellent grade"""
    print("Excellent")


def print_invalid():
    """This function will print an error statement"""
    print("Invalid score")


def collect_user_score():
    """This function will collect users score"""
    score = float(input("Enter score: "))
    return score


main()
