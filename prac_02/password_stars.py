"""
Handwritten code
prints stars for how many characters are input
"""
user_password = input("password: ")
number_of_stars = len(user_password)
while number_of_stars < 8:
    print("Invalid password, too short")
    user_password = input("password: ")
    number_of_stars = len(user_password)

print(number_of_stars * "*")
