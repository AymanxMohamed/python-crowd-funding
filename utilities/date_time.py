from datetime import *


def convert_to_date(str):
    _format = "%d-%m-%Y"
    try:
        return datetime.strptime(str, _format)
    except ValueError as e:
        return None
