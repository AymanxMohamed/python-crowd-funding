from end_points.register import register
from end_points.login import login, logout
import entities.project as project

main_menu_handler = {
    "1": register,
    "2": login,
    "3": exit
}
project_menu_handler = {
    "1": project.create,
    "2": project.view_all,
    "3": project.edit,
    "4": project.delete,
    "5": project.show,
    "6": logout,
    "7": exit
}
menus_options = {
    "main_menu": "123",
    "project_menu": "1234567"
}


def draw_main_menu():
    print("================================================")
    print("\t*______*_____ Main Menu _____*_____*")
    print("================================================")
    print("1: register")
    print("2: login")
    print("3: exit")


def draw_project_menu():
    print("================================================")
    print("\t*______*_____ Projects Menu _____*_____*")
    print("================================================")
    print("1: create new project")
    print("2: view all projects")
    print("3: edit project")
    print("4: delete project")
    print("5: get project")
    print("6: logout")
    print("7: exit")


draw_menu = {
    "main_menu": draw_main_menu,
    "project_menu": draw_project_menu
}


def get_user_choice(menu):
    choice = input("> Please choose an option: ")
    while not choice or choice not in menus_options[menu]:
        choice = input("> Please choose right option: ")
    return choice


def choice_handler(menu):
    if menu == "main_menu":
        return main_menu_handler[get_user_choice("main_menu")]()
    else:
        project.get_all()
        return project_menu_handler[get_user_choice("project_menu")]()

