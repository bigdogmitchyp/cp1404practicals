"""
CP1404 prac module
started 2/11 @ 1200
estimated time 2 days
"""

from project import Project

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")
HEADER = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"


def main():
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            project_file = input("Project file name >>> ")
            with open(project_file, "r") as file:
                file.readline()
                projects = []
                for row in file:
                    name = []
                    row = row.split()
                    for value in range(len(row) - 4):
                        name.append(row[value])
                    name = " ".join(name)
                    row[0] = name
                    del row[1:-4]
                    projects.append(Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
        elif menu_choice == "S":
            project_file = input("Project file name >>> ")
            with open(project_file, "w") as file:
                file.writelines(f"{HEADER}\n")
                for project in projects:
                    file.write(f"{project.name} {project.date} {project.priority} "
                               f"{project.cost} {project.completion}\n")
        elif menu_choice == "D":
            projects.sort(key=lambda project: project.priority)
            print("Incomplete projects:")
            for project in projects:
                if project.is_not_complete():
                    print(f"  {project.name}, start: {project.date}, priority {project.priority}, estimate: "
                          f"${project.cost}, completion: {project.completion}%")
            print("Complete projects:")
            for project in projects:
                if project.is_complete():
                    print(f"  {project.name}, start: {project.date}, priority {project.priority}, estimate: "
                          f"${project.cost}, completion: {project.completion}%")

        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            print("Let's add a new project")
            project_name = input("Name: ")
            project_date = input("Start date (dd/mm/yy): ")
            project_priority = input("Priority: ")
            project_cost = input("Cost estimate: ")
            project_completion = input("Percent complete: ")
            projects.append(Project(project_name, project_date, int(project_priority),
                                    float(project_cost), int(project_completion)))

        elif menu_choice == "U":
            count = -1
            for project in projects:
                count += 1
                print(f"{count} {project.name}, start: {project.date}, priority {project.priority}, estimate: "
                      f"${project.cost}, completion: {project.completion}%")
            project_to_update = int(input("Project choice: "))
            project = projects[project_to_update]
            print(f"  {project.name}, start: {project.date}, priority {project.priority}, estimate: "
                  f"${project.cost}, completion: {project.completion}%")
            completion_to_update = int(input("New Percentage: "))
            priority_to_update = int(input("New Priority: "))
            project.completion = completion_to_update
            project.priority = priority_to_update

        else:
            print("Invalid menu choice!")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software")


main()
