"""This module contains response for each endipoint"""


class GetResponse:
    """This class contains responses for GET method"""
    def __init__(self, order_value=None):
        self.order_value = order_value

    def get_unexist_orders_response(self):
        """Method for unexisting orders responce"""
        return {
            "Message": "Nothing Found",
            "Description": "Orders not created yet",
            "Status": "NOT FOUND"}, 404

    def get_exist_orders_response(self):
        """Method for existing orders responce"""
        return {
            "Orders": self.order_value}, 200

    def get_order_with_invalid_id_response(self):
        """Method for getting order with invalid ID response"""
        return {
            "Message": "Invalid Order ID",
            "Description":
            "Order with ID = {} does not exist".format(self.order_value),
            "Status": "NOT FOUND"}, 404

    def get_order_with_valid_id_response(self):
        """Method for getting order with valid ID response"""
        return {
            "Order": self.order_value}, 200


class PostResponse:
    """This class contains responses for POST method"""
    def __init__(self, invalid_key=None):
        self.invalid_key = invalid_key

    def post_order_with_empty_entries_response(self):
        """Method for post empty order response"""
        return {
            "Message": "Empty Order Not Allowed",
            "Description": "Order can not be created",
            "Status": "NOT ALLOWED"}, 200

    def post_order_with_invalid_item_description_type_and_value_response(self):
        """Method for creating order with invalid item or description response"""
        if self.invalid_key == "item":
            return {
                "Message": "Invalid Order " + str(self.invalid_key).title(),
                "Description": "Order can not be created",
                "Status": "BAD REQUEST"}, 400
        return {
            "Message": "Invalid Order " + str(self.invalid_key).title(),
            "Description": "Order can not be created",
            "Status": "BAD REQUEST"}, 400

    def post_order_with_invalid_quantity_type_and_value_response(self):
        """Method for posting order with invalid quantity response"""
        return {
            "Message": "Invalid Order Quantity",
            "Description": "Order with quantity value <= 0 or string can not be created",
            "Status": "BAD REQUEST"}, 400

    def post_order_with_valid_entries_both_type_and_value_response(self):
        """Method for posting order with valid entries response"""
        return {
            "Message": "Created",
            "Description": "Order Successful Created",
            "Status": "RECEIVED"}, 200


class PutRespose:
    """This class contains responses for PUT method"""
    def __init__(self, order_value=None):
        self.order_value = order_value

    def put_order_with_invalid_id_response(self):
        """Method for updating order with invalid ID response"""
        return {
            "Message": "Invalid Order ID",
            "Description":
            "Order with ID = {} does not exist".format(self.order_value),
            "Status": "NOT FOUND"}, 404

    def put_order_with_empty_entries_response(self):
        """Method for updating order with empty entries response"""
        return {
            "Message": "Empty Status Not Allowed",
            "Description":
            "Order with ID = {}, Status can not be updated"
            .format(self.order_value),
            "Status": "BAD REQUEST"}, 400

    def put_order_with_undefined_status_response(self):
        """Method for updating order with undefined status response"""
        return {
            "Message": "Undefined Order Status",
            "Description":
            "Order with ID = {}, Status can not be updated"
            .format(self.order_value),
            "Status": "UNDEFINED"}

    def put_order_with_valid_status_response(self):
        """Method for updating order with valid status response"""
        return {
            "Message": "Status Updated",
            "Description":
            "Order with ID = {}, Status updated".format(self.order_value),
            "Status": "UPDATED"}, 200


class DeleteResponse:
    """This class contains responses for DELETE method"""
    def __init__(self, order_value=None):
        self.order_value = order_value

    def delete_order_with_invalid_id_response(self):
        """Method for deleting order with invalid ID response"""
        return {
            "Message": "Invalid Order ID",
            "Description":
            "Order with ID = {} does not exist".format(self.order_value),
            "Status": "NOT FOUND"}, 404

    def delete_order_with_valid_id_response(self):
        """Method for deleting order with valid ID response"""
        return {
            "Message": "Order Deleted",
            "Description":
            "Order with ID = {} Deleted Successful".format(self.order_value),
            "Status": "DELETED"}, 200
