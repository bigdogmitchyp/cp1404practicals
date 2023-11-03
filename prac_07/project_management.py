"""
CP1404 prac module
started 2/11 @ 1200
estimated time 2 days
"""

from project import Project

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
        "(A)dd new project)\n(U)pdate project\n(Q)uit")
HEADER = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"


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
                    del row[1:-4]
                    project = Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4]))
                    jobs.append(project)
                    projects = []
                for project in jobs:
                    project = [project.name, project.date, project.priority, project.cost, project.completion]
                    projects.append(project)

        elif menu_choice == "S":
            project_file = input("Project file name >>> ")
            with open(project_file, "w") as file:
                file.writelines(f"{HEADER}\n")
                for project in projects:
                    file.write(f"{project[0]} {project[1]} {project[2]} {project[3]} {project[4]}\n")

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
