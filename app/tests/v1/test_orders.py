"""This module contains ALL testcases for api endpoints in views.py module"""

import json
import pytest

@pytest.mark.parametrize(
    "new_order, status_code", [
        (dict(), 200),
        (dict(item=20), 400),
        (dict(item="Chicken", description=40), 400),
        (dict(item="Chicken", description="Saved with soup", quantity=2), 201)
        ]
    )

def test_create_order_with_valid_entries(test_client, new_order, status_code):
    """This function tests for creating order with all posibilities to return appropriate status code"""
    response = test_client.post("/api/v1/orders", data=json.dumps(new_order))
    assert response.status_code == status_code