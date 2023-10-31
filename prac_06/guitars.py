"""
CP1404 prac module
est time = 30 min
start time =  1516
end time = 1550
total time = 34 min
"""

from guitar import Guitar

print("My guitars")
guitars = []
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: "))
    new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(new_guitar)
    print(f"{new_guitar.name} ({new_guitar.year}) : {new_guitar.cost:,.2f} added")
    guitar_name = input("Name: ")

print("These are my guitars")
for i, guitars in enumerate(guitars, 1):
    if guitars.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitars.name} ({guitars.year}), worth $ {guitars.cost:,.2f}{vintage_string}")
