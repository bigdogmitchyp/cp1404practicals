"""
CP1404 Week 2 Prac
Score menu
"""
MENU = """(G)ive Score (0-100)\n(P)rint result\n(S)how stars\n(Q)uit"""


def main():
    score = assign_blank_score()
    display_menu()
    choice = collect_user_choice()
    check_menu_choice(choice, score)


def collect_user_choice():
    choice = input(">>> ").upper()
    return choice


def assign_blank_score():
    score = ""
    return score


def display_menu():
    print(MENU)


def check_menu_choice(choice, score):
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
    print("Bye Bye")


def print_invalid():
    print("Invalid choice")


def collect_user_score():
    score = float(input("Enter Score: "))
    return score


def return_stars(score):
    if score == "":
        print("No score given")
    elif score > 100 or score < 0:
        print("Invalid score")
    else:
        print(int(score) * "*")


def return_grade(score):
    if score == "":
        print("No score given")
    elif score > 100 or score < 0:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
