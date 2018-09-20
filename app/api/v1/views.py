"""This module contains all api endpoints"""
# Thirdparty imports
from datetime import datetime
from flask import request
from flask_restful import Resource

# Local imports
from .models import ORDERS_DATA
from .validators import OrderItemsValodator

DATE = datetime.now().strftime("%B %d, %Y")
STATUS_CODE = 0  # received


class Orders(Resource):
    """Class that creates orders and list all orders"""

    def post(self):
        """Method for order creation"""
        pass
