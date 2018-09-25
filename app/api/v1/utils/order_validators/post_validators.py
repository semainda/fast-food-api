"""This module contains validations for order items"""

# Thirdparty imports
import re

def order_str_data_validator(**kwargs):
    validation_output = ""
    for key in kwargs:
        if not re.fullmatch(r"^[a-zA-Z ]+$", str(kwargs[key])) and isinstance(kwargs[key], str):
            validation_output = False, key
            break
        validation_output = True,
    return validation_output

def order_int_data_validator(qty):
    return re.fullmatch(r"[1-9]\d*$", str(qty)) and isinstance(qty, int)