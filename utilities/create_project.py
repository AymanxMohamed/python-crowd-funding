import entities.project as project
from utilities.Validator import Validator
from datetime import *


def get_title():
    title = input("> Please Enter The project title: ")
    while project.exists(title) or not Validator.validate_title(title):
        print("> This project title already exists or You entered invalid title name !!")
        print("> please use only alphabetic chars")
        title = input("> Please Enter a new  project title: ")
    return title.strip()


def get_details():
    details = input("> Please Enter The project details: ")
    while not details:
        print("> details can't be empty !!")
        details = input("> Please Enter The project details: ")
    return details


def get_total_target():
    total_target = input("> Please Enter the total project target: ")
    while not total_target.isdigit():
        total_target = input("> Please Enter a correct  project target: ")
    return total_target


def get_start_time():
    start_time = input("Please Enter the start date in the form of dd-mm-yyyy: ")
    while not Validator.validate_datetime(start_time):
        print("The start time must be in the form of dd-mm-yyyy !! and valid time after (now)")
        start_time = input("Please Enter the start date in the form of dd-mm-yyyy: ")
    return start_time


def get_end_time(start_time):
    _format = "%d-%m-%Y"
    end_time = input("Please Enter the end date in the form of dd-mm-yyyy: ")
    while not Validator.validate_datetime(start_time):
        print("The end time must be in the form of dd-mm-yyyy !!")
        end_time = input("Please Enter the end date in the form of dd-mm-yyyy: ")
    _start_time = datetime.strptime(start_time, _format)
    _end_time = datetime.strptime(end_time, _format)
    if _start_time > _end_time:
        print("End Time must came after start time")
        get_end_time(start_time)
    return end_time


def get_project_data():
    from entities.user import main_user as user
    title = get_title()
    details = get_details()
    total_target = get_total_target()
    start_time = get_start_time()
    end_time = get_end_time(start_time)

    return {
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_time": start_time,
        "end_time": end_time,
        "user_email": user['email']
    }
