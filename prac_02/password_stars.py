"""
Handwritten code
prints stars for how many characters are input
"""


def main():
    """This function prints stars for number of characters given"""
    number_of_stars = get_password()
    print_stars(number_of_stars)


def print_stars(number_of_stars):
    """This function prints stars"""
    print(number_of_stars * "*")


def get_password():
    """This function collects users password"""
    user_password = input("password: ")
    number_of_stars = number_of_stars_length(user_password)
    return check_error(number_of_stars)


def number_of_stars_length(user_password):
    """This function counts the number of characters in user password"""
    number_of_stars = len(user_password)
    return number_of_stars


def check_error(number_of_stars):
    """This function checks that the password is not shorter than eight characters"""
    while number_of_stars < 8:
        print_invalid()
        get_password()
    return number_of_stars


def print_invalid():
    """This function prints invalid"""
    print("Invalid password, too short")


main()
