"""
CP1404 Practical
Estimate: 30 min
Actual: 21 min
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ")
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    start = email.split("@")[0]
    parts = start.split(".")
    name = " ".join(parts).title()
    return name


main()
