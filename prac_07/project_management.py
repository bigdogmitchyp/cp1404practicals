"""
CP1404 prac module
started 2/11 @ 1200
estimated time 2 days
"""

import datetime
from project import Project

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    print(MENU)
    menu_choice = input(">>> ").upper()
    project_file = "projects.txt"
    projects = load_projects(project_file)
    while menu_choice != "Q":
        if menu_choice == "L":
            project_file = get_valid_input("Load project file>>> ")
            projects = load_projects(project_file)
        elif menu_choice == "S":
            project_file = get_valid_input("Save to project file>>> ")
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


def get_valid_input(display_message):
    user_input = input(display_message)
    while user_input == "" or user_input.isspace():
        print("Input cannot be blank!")
        user_input = input(display_message)
    return user_input


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
        print(f"{count} {project.name}, start: {project.date}, priority {project.priority},"
              f" estimate: ${project.cost}, completion: {project.completion}%")
    project_to_update = get_valid_number("Project choice: ")
    while project_to_update not in range(0, len(projects)):
        print("Invalid choice")
        project_to_update = get_valid_number("Project choice: ")
    project = projects[project_to_update]
    print_project_without_indent(project)
    new_percent = input("New Percentage: ")
    if new_percent == "":
        pass
    else:
        while new_percent.isalpha():
            print("Please pick a number!")
            new_percent = input("New Percentage: ")
        new_percent = int(new_percent)
        project.completion = new_percent
    new_prio = input("New Priority: ")
    if new_prio == "":
        pass
    else:
        while new_prio.isalpha():
            print("Please pick a number!")
            new_prio = input("New Priority: ")
        new_prio = int(new_prio)
        project.priority = new_prio


def filter_projects_by_date(projects):
    date_input = get_valid_date("Show projects that start after date (d/m/yy): ")
    date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
    projects.sort(key=lambda project: datetime.datetime.strptime(project.date, "%d/%m/%Y").date())
    for project in projects:
        if date <= datetime.datetime.strptime(project.date, "%d/%m/%Y").date():
            print_project_without_indent(project)


def get_valid_date(display_message):
    is_input_valid = False
    while not is_input_valid:
        try:
            date_input = get_valid_input(display_message)
            if datetime.datetime.strptime(date_input, "%d/%m/%Y").date():
                is_input_valid = True
        except ValueError:
            print("Invalid date format!")
    return date_input


def add_project(projects):
    print("Let's add a new project")
    project_name = get_valid_input("Name: ")
    date_input = get_valid_date("Start date (dd/mm/yy): ")
    project_priority = get_valid_number("Priority: ")
    project_cost = float(get_valid_number("Cost estimate: "))
    project_completion = get_valid_number("Percent complete: ")
    projects.append(Project(project_name, date_input, int(project_priority),
                            float(project_cost), int(project_completion)))


def print_project_without_indent(project):
    print(f"{project.name}, start: {project.date}, priority {project.priority}, estimate: "
          f"${project.cost}, completion: {project.completion}%")


def print_project_with_indent(project):
    print(f"  {project.name}, start: {project.date}, priority {project.priority}, estimate: "
          f"${project.cost}, completion: {project.completion}%")


def save_projects(project_file, projects):
    with open(project_file, "w", encoding="utf-8") as file:
        file.writelines("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.date}\t{project.priority}\t"
                       f"{project.cost}\t{project.completion}\n")


def load_projects(project_file):
    is_valid_input = False
    while not is_valid_input:
        try:
            with open(project_file, "r", encoding="utf-8") as file:
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
                    projects.append(Project(row[0], row[1], int(row[2]),
                                            float(row[3]), int(row[4])))
                is_valid_input = True
        except FileNotFoundError:
            print("Invalid file name!")
            project_file = get_valid_input("Load project file>>> ")
    return projects


def get_valid_number(display_message):
    """Gets valid number from user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = int(get_valid_input(display_message))
            is_valid_input = True
        except ValueError:
            print("Please enter a valid number!")
    return user_input


main()
