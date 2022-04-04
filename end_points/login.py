import entities.user as user
from security.password_hash import verify_password


def get_email():
    counter = 0
    email = input("> Please Enter your email: ")
    while not user.exists(email):
        if counter == 2:
            return None
        counter += 1
        print("> This email doesn't exits !!")
        email = input("enter a correct email: ")
    return email


def is_authorized(logged_user):
    counter = 0
    password = input("> Please Enter your password: ")
    while not verify_password(password, logged_user['password']):
        if counter == 2:
            return False
        counter += 1
        print("> Wrong password !!")
        password = input("> enter a correct password: ")
    user.main_user = logged_user
    return True


def login():
    print("================================================")
    print("\t*______*_____ Login  _____*_____*")
    print("================================================")
    email = get_email()
    if not email:
        return "main_menu"
    logged_user = user.get_user(email)
    if not is_authorized(logged_user):
        return "main_menu"
    user.main_user = logged_user
    print("================================================")
    print(f"*______*_____ Welcome { logged_user['first_name'] } { logged_user['last_name'] } _____*_____*")
    return "project_menu"


def logout():
    print("================================================")
    print(f"*______*_____ We will miss you 😢 _____*_____*")
    user.main_user = None
    return "main_menu"

