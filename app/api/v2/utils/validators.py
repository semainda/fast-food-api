"""Module that validates strings and intergers"""

import re

def input_validators(**kwargs):
    validation_output = ""
    for key in kwargs:
        if isinstance(kwargs[key], str):
            if not re.fullmatch(r"^[a-zA-Z ]+$", str(kwargs[key])) and isinstance(kwargs[key], str):
                validation_output = False, key
                break
            validation_output = True,
        if not re.fullmatch(r"[1-9]\d*$", str(kwargs[key])) and isinstance(kwargs[key], int):
            validation_output = False, key
            break
        validation_output = True,
    return validation_output
