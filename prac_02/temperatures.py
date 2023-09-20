"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""


def main():
    """This function will display a menu that converts temperatures"""
    choice = display_menu()
    check_menu_input(choice)
    print_final_message()


def print_final_message():
    """This function prints thank you when the user is done"""
    print("Thank you.")


def check_menu_input(choice):
    """This function checks user inputs and runs corresponding functions"""
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_c_to_f()
            print_fahrenheit(fahrenheit)
        elif choice == "F":
            celsius = convert_f_to_c()
            print_celsius(celsius)
        else:
            print_error()
        display_menu()


def print_error():
    """This menu prints error when and invalid option is input"""
    print("Invalid option")


def print_celsius(celsius):
    """This function prints the Celsius value"""
    print(f"Result: {celsius:.2f} C")


def print_fahrenheit(fahrenheit):
    """This function prints the Fahrenheit value"""
    print(f"Result: {fahrenheit:.2f} F")


def convert_f_to_c():
    """This function converts Fahrenheit to Celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_c_to_f():
    """This function converts Celsius to Fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def display_menu():
    """This function prints the menu"""
    print(MENU)
    choice = input(">>> ").upper()
    return choice


main()
