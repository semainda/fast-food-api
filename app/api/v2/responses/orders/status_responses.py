"""Module that hold order status responses"""


class StatusResponse:
    """Class that contains responses regarding order status"""
    def __init__(self, status_code, status_value=None):
        self.status_code = status_code
        self.status_value = status_value
    
    def status_does_not_exist_response(self):
        return {
            "Message": "'{}' is invalid status code.".format(self.status_code),
            }, 404
    
    def order_with_status_code_does_not_exist_response(self):
        return {
            "Message": "Order with status code '{}' does not exist."\
            .format(self.status_code),
            "Description": "There is no order which is '{}'."\
            .format((self.status_value).title())
            }, 404