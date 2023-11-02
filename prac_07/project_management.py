"""
CP1404 prac module
started 2/11 @ 1200
estimated time 2 days
"""

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
        "(A)dd new project)\n(U)pdate project\n(Q)uit")

from project import Project

def main():
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            project_file = input("Project file name >>> ")
            with open(project_file, "r") as file:
                file.readline()
                jobs = []
                for row in file:
                    name = []
                    row = row.split()
                    for value in range(len(row) - 4):
                        name.append(row[value])
                    name = " ".join(name)
                    row[0] = name
                    for value in row:
                        del row[1:-4]
                    project = Project(row[0], row[1], row[2], row[3], row[4])
                    jobs.append(project)

        elif menu_choice == "S":
            pass
        elif menu_choice == "D":
            pass
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        else:
            print("Invalid menu choice!")
        print(MENU)
        menu_choice = input(">>> ").upper()

main()