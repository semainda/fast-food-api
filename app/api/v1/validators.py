"""This module contains validations for order items"""

# Thirdparty imports
import re


class OrderItemsValodator:
    """Class for validation of order items"""

    def __init__(self, text=None, number=0):
        """This constructor initializes order items"""
        self.text = text
        self.number = number

    def text_validator(self):
        """Function for text/string validations"""
        regex = r"^[a-zA-Z ]+$"
        return re.fullmatch(
            regex, str(self.text)) and isinstance(self.text, str)

    def number_validator(self):
        """Function for number/integer validations"""
        regex = r"[1-9]\d*$"
        print(re.fullmatch(
            regex, str(self.number)) and isinstance(self.number, int))
