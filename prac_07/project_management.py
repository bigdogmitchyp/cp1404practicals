"""
CP1404 prac module
started 2/11 @ 1200
estimated time 2 days
"""

from project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")
HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"


def main():
    print(MENU)
    menu_choice = input(">>> ").upper()
    project_file = "projects.txt"
    projects = load_projects(project_file)
    while menu_choice != "Q":
        if menu_choice == "L":
            project_file = input("Project file name >>> ")
            projects = load_projects(project_file)
        elif menu_choice == "S":
            project_file = input("Project file name >>> ")
            save_projects(project_file, projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects_by_date(projects)
        elif menu_choice == "A":
            add_project(projects)
        elif menu_choice == "U":
            update_project_info(projects)
        else:
            print("Invalid menu choice!")
        print(MENU)
        menu_choice = input(">>> ").upper()
    save_projects(project_file, projects)
    print("Thank you for using custom-built project management software")


def display_projects(projects):
    projects.sort(key=lambda project: project.priority)
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print_project_with_indent(project)
    print("Complete projects:")
    for project in projects:
        if project.is_complete():
            print_project_with_indent(project)


def update_project_info(projects):
    count = -1
    for project in projects:
        count += 1
        print(f"{count} {project.name}, start: {project.date}, priority {project.priority}, estimate: "
              f"${project.cost}, completion: {project.completion}%")
    project_to_update = int(input("Project choice: "))
    project = projects[project_to_update]
    print_project_without_indent(project)
    completion_to_update = int(input("New Percentage: "))
    priority_to_update = int(input("New Priority: "))
    project.completion = completion_to_update
    project.priority = priority_to_update


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (d/m/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    projects.sort(key=lambda project: datetime.datetime.strptime(project.date, "%d/%m/%Y").date())
    for project in projects:
        if date <= datetime.datetime.strptime(project.date, "%d/%m/%Y").date():
            print_project_without_indent(project)


def add_project(projects):
    print("Let's add a new project")
    project_name = input("Name: ")
    project_date = input("Start date (dd/mm/yy): ")
    project_priority = input("Priority: ")
    project_cost = input("Cost estimate: ")
    project_completion = input("Percent complete: ")
    projects.append(Project(project_name, project_date, int(project_priority),
                            float(project_cost), int(project_completion)))


def print_project_without_indent(project):
    print(f"{project.name}, start: {project.date}, priority {project.priority}, estimate: "
          f"${project.cost}, completion: {project.completion}%")


def print_project_with_indent(project):
    print(f"  {project.name}, start: {project.date}, priority {project.priority}, estimate: "
          f"${project.cost}, completion: {project.completion}%")


def save_projects(project_file, projects):
    with open(project_file, "w") as file:
        file.writelines(f"{HEADER}\n")
        for project in projects:
            file.write(f"{project.name}\t{project.date}\t{project.priority}\t"
                       f"{project.cost}\t{project.completion}\n")


def load_projects(project_file):
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
    return projects


main()
