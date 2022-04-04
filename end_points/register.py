# first get user info
# first name ✅
# last name ✅
# email (unique)
#   1- you have to validate email ✅
#   2- you have to check if the email already exists or not ✅
# password ✅
# confirm password ✅
#   check if the passwords match a certain regx and matched each others ✅
#   hash the password before storing it ✅
# mobile phone ✅
#   validate the phone number against Egypt phone numbers ✅
from utilities.user_info import get_user_data


def register():
    print("================================================")
    print("\t*______*_____ Register _____*_____*")
    print("================================================")
    with open("data/users.txt", "a") as users_file:
        users_file.write(f"{ get_user_data() }\n")
    return "main_menu"


