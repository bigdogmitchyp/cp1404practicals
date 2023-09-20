"""
Handwritten code
prints stars for how many characters are input
"""


def main():
    """This function prints stars for number of characters given"""
    number_of_stars = get_password()
    print_stars(number_of_stars)


def print_stars(number_of_stars):
    print(number_of_stars * "*")


def get_password():
    user_password = input("password: ")
    number_of_stars = len(user_password)
    while number_of_stars < 8:
        print("Invalid password, too short")
        user_password = input("password: ")
        number_of_stars = len(user_password)
    return number_of_stars


main()
