"""This module contains ALL testcases for api endpoints in views.py module"""
# Thirdparty imports
import json
import pytest


def test_request_orders_which_does_not_exist(test_client):
    """Tests for requesting orders which does not exist to return 404"""
    response = test_client.get("/api/v1/orders")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "new_order, status_code", [
        (dict(), 200),
        (dict(item=20), 400),
        (dict(item="Chicken", description=40), 400),
        (dict(item="Chicken", description="Saved with soup", quantity=2), 201)
        ]
    )
def test_create_order(test_client, new_order, status_code):
    """Test for creating order with all posibilities
    to return appropriate status code"""
    response = test_client.post("/api/v1/orders", data=json.dumps(new_order))
    assert response.status_code == status_code


def test_request_orders_which_does_exist(test_client):
    """Test for requesting orders which does not exist to return 404"""
    response = test_client.get("/api/v1/orders")
    assert response.status_code == 200


def test_request_invalid_order(test_client):
    """Tests for requesting order with invalid ID that does not exist
    to return 404"""
    response = test_client.get("/api/v1/orders/2000000")
    response.status_code == 404


def test_request_valid_order(test_client):
    """Test for requesting valid order to  return 200"""
    response = test_client.get("/api/v1/orders/1")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "order_id, order_status, status_code", [
        (3000, dict(), 404),
        (1, dict(), 400),
        (1, dict(status=1), 200)
        ]
    )
def test_update_order(test_client, order_id, order_status, status_code):
    """Test for updating order with four posibilities
    to return appropriate status code"""
    response = test_client.put(
        "/api/v1/orders/order_id", data=json.dumps(order_status))
    assert response.status_code == status_code


@pytest.mark.parametrize("order_id, status_code", [(1, 200), (3000, 404)])
def test_delete_order(test_client, order_id, status_code):
    """Tests for deleting valid order to  return 200 or 404"""
    response = test_client.delete("/api/v1/orders/order_id")
    assert response.status_code == status_code
