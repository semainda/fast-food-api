"""Module that holds meal order responses"""


class OrderResponses:
    """Class that hold all order responses"""
    def unlogged_in_user_response(self):
        """Method that returns incorrect login"""
        return {"Message": "Sorry! Your not logged in"}, 401

    def create_order_with_invalid_contents_response(self, item):
        """Method for invalid responses"""
        return {
            "Message": "Order '{}' is invalid for it to be created"\
            .format(item)}, 400
    
    def order_created_response(self, order):
        """Method for created response"""
        return {
            "Message": "Order with id '{}' created successful"\
            .format(order)}, 201

    def exists_user_orders_response(self, orders):
         """Method that returns user orders not found"""
         return {"Orders": orders}, 200

    def exists_user_order_response(self, order, status):
        """Method that returns user order not found"""
        return {
                "Id": order[0], "Name": order[1] + " " + order[2],
                "Meal": order[3], "Quantity": order[4],
                "Description": order[5], 
                "Status": status, "Delivery Address": order[7],
                "Created Date": str(order[8]),
                "Delivery Time": str(order[9])
                }, 200
    
    def user_orders_does_not_exists_response(self):
        """Method that returns user orders not found"""
        return {"Message": "Sorry! orders history is empty"}, 404
    
    def user_order_does_not_exists_response(self, order_id):
        """Method that returns user orders not found"""
        return {"Message": "Order with id '{}' does not exist".format(order_id)}, 404
    
    def forbidden_user_access_response(self):
        """Method for returning unauthorized response"""
        return {
            "Message": "Your access is denied to this resource"
        }, 403   
    
    def order_updated_response(self, order_id):
        """Method for updated response"""
        return {
            "Message": "Order with '{}' updated successful"\
            .format(order_id)}, 201
    
    def request_order_does_not_exists_response(self, order_id):
        """Method that returns categories not found"""
        return {"Message": "Order with id '{}' does not exists".format(order_id)}, 404