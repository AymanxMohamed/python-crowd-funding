from utilities.Validator import Validator
from security.password_hash import hash_password
import entities.user as user


def get_user_name(prompt):
    name = input(prompt)
    while not Validator.validate_name(name):
        name = input("> Please Enter a correct name: ")
    return name


def get_user_email():
    email = input("> Please Enter your Email: ")
    while user.exists(email):
        print("> This email already exists !!")
        email = input("> Please Enter The Email again: ")
    while not Validator.validate_email(email):
        email = input("> Please Enter a valid email: ")
    return email


def user_password():
    password = input("> Please Enter Your Password: ")
    while not Validator.validate_password(password):
        print("> password must contains at least 1 capital chars and special chars  and also at least 8 chars !!")
        password = input("> Please Enter Your Password Again: ")
    return password


def get_user_password():
    while True:
        password = user_password()
        password_confirmation = input("> Please Confirm Your Password: ")
        if password_confirmation == password:
            return password
        else:
            print("> Password doesn't match !!")


def get_user_mobile():
    mobile = input("> Please Enter Your Mobile phone: ")
    while not Validator.validate_mobile(mobile):
        mobile = input("> Please Enter a valid mobile number: ")
    return mobile


def get_user_data():
    return {
        "first_name": get_user_name("> Please Enter your first name: "),
        "last_name": get_user_name("> Please Enter your last name: "),
        "email": get_user_email(),
        "password": hash_password(get_user_password()),
        "mobile": get_user_mobile()
    }
