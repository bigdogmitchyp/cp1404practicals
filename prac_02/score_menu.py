"""
CP1404 Week 2 Prac
Score menu
"""
MENU = """(G)ive Score (0-100)\n(P)rint result\n(S)how stars\n(Q)uit"""


def main():
    """This function executes the score menu functions"""
    score = assign_blank_score()
    display_menu()
    choice = collect_user_choice()
    check_menu_choice(choice, score)


def collect_user_choice():
    """This function collects the users menu selection"""
    choice = input(">>> ").upper()
    return choice


def assign_blank_score():
    """This function assigns a blank score so that the menu will work"""
    score = ""
    return score


def display_menu():
    """This function will print the menu"""
    print(MENU)


def check_menu_choice(choice, score):
    """This function executes functions based on user inputs"""
    while choice != "Q":
        if choice == "G":
            score = collect_user_score()
        elif choice == "P":
            return_grade(score)
        elif choice == "S":
            return_stars(score)
        else:
            print_invalid()
        display_menu()
        collect_user_choice()
    print_bye()


def print_bye():
    """This function prints bye bye"""
    print("Bye Bye")


def print_invalid():
    """This function prints invalid choice"""
    print("Invalid choice")


def collect_user_score():
    """This function collects user score"""
    score = float(input("Enter Score: "))
    return score


def return_stars(score):
    """This function prints stars"""
    if score == "":
        print_no_score()
    elif score > 100 or score < 0:
        print_invalid()
    else:
        draw_stars(score)


def draw_stars(score):
    """This function draws stars for users score"""
    print(int(score) * "*")


def print_no_score():
    """This function will print no score given"""
    print("No score given")


def return_grade(score):
    """This function assigns grades to scores"""
    if score == "":
        print_no_score()
    elif score > 100 or score < 0:
        print_invalid()
    elif score >= 90:
        print_excellent()
    elif score >= 50:
        print_passable()
    else:
        print_bad()


def print_bad():
    """This function prints bad"""
    print("Bad")


def print_passable():
    """This function prints passable"""
    print("Passable")


def print_excellent():
    """This function prints excellent"""
    print("Excellent")


main()
