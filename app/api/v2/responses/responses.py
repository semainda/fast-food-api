"""This module contains response for each endipoint"""


def resource_does_not_exist_response():
    """Method for resouce not found responce"""
    return {"Message": "The requested resource does not exist"}, 404


def resource_already_exist_response():
    """Method for exist response """
    return {"Message": "The resource already exist"}, 200


def resource_with_empty_entries_response():
    """Method for post empty order response"""
    return {"Message": "Create empty resources is not allowed"}, 200


def resource_with_invalid_entries_response():
    """Method for  response"""
    return {"Message": "Invalid resource supplied"}, 400


def resource_success_response():
    """Method for updated response"""
    return {"Message": "Resource processed successful"}, 200
