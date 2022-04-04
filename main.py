from utilities.menus import draw_menu, choice_handler


def main():
    menu = "main_menu"
    while True:
        draw_menu[menu]()
        menu = choice_handler(menu)


main()
