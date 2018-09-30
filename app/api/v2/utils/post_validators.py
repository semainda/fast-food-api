"""This module contains validations for order items"""

# Thirdparty imports
import re

def order_str_data_validator(**kwargs):
    validation_output = ""
    for key in kwargs:
        if not re.fullmatch(r"^[a-zA-Z ]+$", str(kwargs[key])) and isinstance(kwargs[key], str):
            validation_output = False
            break
        validation_output = True
    return validation_output

# def order_int_data_validator():
    # return re.fullmatch(r"[1-9]\d*$", str(number)) and isinstance(number, int)

def order_int_data_validator(**kwargs):
    validation_output = ""
    for key in kwargs:
        if not re.fullmatch(r"[1-9]\d*$", str(number)) and isinstance(number, int):
            validation_output = False
            break
        validation_output = True
    return validation_output