"""This module contains ALL testcases for api endpoints in views.py module"""
# Thirdparty imports
import json
import pytest


def test_unexisting_orders(test_client):
    """Tests for requesting orders which does not exist to return 404"""
    response = test_client.get("/api/v1/orders")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "new_order, status_code", [
        ("", 400),
        (dict(), 400),
        (dict(description="Saved with soup", quantity=2), 400),
        (dict(item="BBQ", quantity=2), 400),
        (dict(item="BBQ", description="Saved with soup"), 400),
        (dict(item="?BBQ", description="Saved with soup", quantity=2), 400),
        (dict(item="BBQ", description="Saved with soup%", quantity=2), 400),
        (dict(item="BBQ", description="Saved with soup", quantity=-2), 400),
        (dict(item="Chicken", description="Saved with soup", quantity=2), 200)
        ]
    )
def test_create_order(test_client, new_order, status_code):
    """Test for creating order with all posibilities
    to return appropriate status code"""
    response = test_client.post(
        "/api/v1/orders", data=json.dumps(new_order),
        headers={"content-type": "application/json"})
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "order_id, status_code", [
        ("abd", 404), (1, 200), (30000, 404)
        ]
    )
def test_get_specific_order(test_client, order_id, status_code):
    """Test for requesting valid order to  return 200"""
    response = test_client.get("/api/v1/orders/" + str(order_id))
    assert response.status_code == status_code


def test_update_with_invalid_url_order(test_client):
    """Test for creating order with all posibilities
    to return appropriate status code"""
    response = test_client.put("/api/v1/orders")
    assert response.status_code == 405


def test_update_with_only_url_order(test_client):
    """Test for creating order with all posibilities
    to return appropriate status code"""
    response = test_client.put("/api/v1/orders/")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "order_id, order_status, status_code", [
        ("an", dict(), 404),
        (1, "", 400),
        (1, dict(), 400),
        (1, dict(), 400),
        (20000, dict(status="Accepted"), 404),
        (1, dict(status="Done"), 200),
        (1, dict(status="Accepted"), 200)
        ]
    )
def test_update_order(test_client, order_id, order_status, status_code):
    """Test for updating order with four posibilities
    to return appropriate status code"""
    response = test_client.put(
        "/api/v1/orders/" + str(order_id), data=json.dumps(order_status),
        headers={"content-type": "application/json"})
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "order_id, status_code", [
        (1, 200), (3000, 404)
        ]
    )
def test_delete_order(test_client, order_id, status_code):
    """Tests for deleting valid order to  return 200 or 404"""
    response = test_client.delete("/api/v1/orders/" + str(order_id))
    assert response.status_code == status_code


def test_delete_order_invalid_url(test_client):
    """Tests for deleting valid order to  return 200 or 404"""
    response = test_client.delete("/api/v1/orders")
    assert response.status_code == 405


def test_delete_order_invalid_url_again(test_client):
    """Tests for deleting valid order to  return 200 or 404"""
    response = test_client.delete("/api/v1/orders/")
    assert response.status_code == 404
