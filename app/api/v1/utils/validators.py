"""This module contains validations for order items"""

# Thirdparty imports
import re


class OrderItemsValodator:
    """Class for validation of order items"""

    def __init__(self, value):
        """This constructor initializes order items"""
        self.value = value
        
    def is_string_validator(self):
        """Method for text/string validations"""
        regex = r"^[a-zA-Z ]+$"
        return re.fullmatch(
            regex, str(self.value)) and isinstance(self.value, str)

    def is_int_validator(self):
        """This method performs validation on quantity"""
        regex = r"[1-9]\d*$"
        return re.fullmatch(regex, str(self.value)) and isinstance(self.value, int)
