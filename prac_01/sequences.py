x = int(input("x input?: "))
y = int(input("y input?: "))
MENU_STRING = "(E)ven numbers\n(O)dd numbers\n(S)quares\n(Q)uit"
print(MENU_STRING)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        if x % 2 == 1:
            x += 1
        for i in range(x, y+1, 2):
            print(i, end=" ")
        print()
        x -= 1
        if x % 2 == 0:
            for i in range(x, y + 1, 2):
                print(i, end=" ")
            print()
    if choice == "O":
        if x % 2 == 0:
            x += 1
            for i in range(x, y+1, 2):
                print(i, end=" ")
            print()
            x -= 1
        else:
            for i in range(x, y+1, 2):
                print(i, end=" ")
            print()
    if choice == "S":
        for i in range(x, y + 1, 1):
            print(i ** 2, end=" ")
        print()
    print(MENU_STRING)
    choice = input(">>> ").upper()
print("Finished.")
