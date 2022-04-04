import os
from utilities.create_project import *


def edit_title(_project):
    _project["title"] = get_title()


def edit_details(_project):
    _project["details"] = get_details()


def edit_total_target(_project):
    _project["total_target"] = get_total_target()


def edit_start_time(_project):
    _project["start_time"] = get_start_time()


def edit_end_time(_project):
    _project["end_time"] = get_end_time(_project["start_time"])


def submit(_proj):
    from entities.project import user_projects
    os.remove("data/projects.txt")
    for _project in user_projects:
        with open("data/projects.txt", "a") as projects_file:
            projects_file.write(f"{_project}\n")
    return 0


edit_project = {
    "title": edit_title,
    "details": edit_details,
    "total_target": edit_total_target,
    "start_time": edit_start_time,
    "end_time": edit_end_time,
    "0": submit,
}


def get_edit_key():
    print("Note: press 0 to submit edit")
    key = input("> pLease Specify the key you want to edit: ")
    while key not in list(edit_project.keys()):
        print("> invalid key !!")
        key = input("> pLease Specify the correct key you want to edit: ")
    return key
