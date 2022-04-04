import ast

users_data = open("data/users.txt", "r")
users = users_data.readlines()
main_user = None


def exists(user_email):
    for user_line in users:
        user = ast.literal_eval(user_line)
        if user_email.lower() == user['email'].lower():
            return True
    return False


def get_user(email):
    for user_line in users:
        user = ast.literal_eval(user_line)
        if email.lower() == user['email'].lower():
            return user
    return None
