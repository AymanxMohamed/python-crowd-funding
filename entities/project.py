import ast

from utilities.edit_remove_project import *
from utilities.date_time import convert_to_date
user_projects = []


def get_projects():
    projects_data = open("data/projects.txt", "r")
    projects = projects_data.readlines()
    projects_data.close()
    return projects


def create():
    print("================================================")
    print("\t*______*_____ Create Project _____*_____*")
    print("================================================")
    with open("data/projects.txt", "a") as users_file:
        from utilities.create_project import get_project_data
        users_file.write(f"{ get_project_data() }\n")
        get_all()
    return "project_menu"


def get_all():
    user_projects.clear()
    from entities.user import main_user as user
    for project_line in get_projects():
        _project = ast.literal_eval(project_line)
        if _project['user_email'].lower() == user['email'].lower():
            user_projects.append(_project)


def view_all():
    print("================================================")
    if not user_projects:
        print("You don't have any projects !!")
        return "project_menu"
    print_projects(user_projects)
    return "project_menu"


def has_projects():
    return user_projects


def delete():
    if not has_projects():
        print("You don't have any projects !!")
        return "project_menu"
    _project = get_required_project()
    if not _project:
        print("invalid project title")
        return "project_menu"
    user_projects.remove(_project)
    submit(_project)
    return "project_menu"


def show():
    start_time = input("Please Enter the start date in the form of dd-mm-yyyy: ")
    projects = get_projects_by_date(start_time)
    if not projects:
        print("You don't have any projects in this date !!")
        return "project_menu"
    print_projects(projects)
    return "project_menu"

def get_project(title):
    print(user_projects)
    for _project in user_projects:
        if _project['title'].lower() == title.lower():
            return _project
    return None


def get_projects_by_date(__date):
    projects = []
    _date = convert_to_date(__date)
    if not _date:
        return projects
    for _project in user_projects:
        start_date = convert_to_date(_project['start_time'])
        if start_date == _date:
            projects.append(_project)
    return projects


def get_required_project():
    counter = 0
    _project = get_project(input("please specify the project title: "))
    while not project:
        if counter == 2:
            return None
        print("You don't have a project with this title !!")
        _project = get_project(input("please enter a correct project title: "))
    return _project


def print_project(_project):
    for i, key in enumerate(_project):
        print(f"{i + 1}: {key} => {_project[key]}")


def edit():
    if not user_projects:
        print("You don't have any projects !!")
        return "project_menu"
    _project = get_required_project()
    if not _project:
        print("invalid project title")
        return "project_menu"
    while True:
        print_project(_project)
        if edit_project[get_edit_key()](_project) == 0:
            return "project_menu"


def exists(title):
    for project_line in get_projects():
        _project = ast.literal_eval(project_line)
        if _project['title'].lower() == title.lower():
            return True
    return False


def print_projects(projects):
    for i, _project in enumerate(projects):
        print(f"""> project no. { i + 1 }:
            Title: { _project['title'] }
            Details: { _project['details'] }
            Total Target: { _project['total_target'] }
            Start Time: { _project['start_time'] }
            End Time: { _project['end_time'] }""")

