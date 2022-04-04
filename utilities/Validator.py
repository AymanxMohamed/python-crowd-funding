import re
from utilities import regx
from datetime import *


class Validator:
    @staticmethod
    def validate_name(name):
        return name.replace(" ", "").isalpha()

    @staticmethod
    def validate_email(email):
        return re.fullmatch(regx["email"], email)

    @staticmethod
    def validate_password(password):
        return re.fullmatch(regx["password"], password)

    @staticmethod
    def validate_mobile(mobile):
        return re.fullmatch(regx["mobile"], mobile)

    @staticmethod
    def validate_title(title):
        return re.fullmatch(regx["title"], title)

    @staticmethod
    def validate_datetime(_datetime):
        now = datetime.now()
        _format = "%d-%m-%Y"
        try:
            _date = datetime.strptime(_datetime, _format)
            isvalid = bool(_date)
            if _date < now:
                isvalid = False
        except ValueError:
            isvalid = False
        return isvalid

