"""This module contains ALL testcases for api endpoints in views.py module"""
# Thirdparty imports
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
    """Test for creating order with all posibilities
    to return appropriate status code"""
    response = test_client.post("/api/v1/orders", data=json.dumps(new_order))
    assert response.status_code == status_code


def test_request_orders_which_does_not_exist(test_client):
    """Tests for requesting orders which does not exist to return 404"""
    response = test_client.get("/api/v1/orders")
    assert response.status_code == 404


def test_request_orders_which_does_exist(test_client):
    """Test for requesting orders which does not exist to return 404"""
    response = test_client.get("/api/v1/orders")
    assert response.status_code == 200


def test_request_valid_order(test_client):
    """Test for requesting valid order to  return 200"""
    response = test_client.get("/api/v1/orders/1")
    assert response.status_code == 200


def test_request_invalid_order(test_client):
    """Tests for requesting order with invalid ID that does not exist
    to return 404"""
    response = test_client.get("/api/v1/orders/20")
    response.status_code == 404