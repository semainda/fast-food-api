"""Module that create test cases for meal"""

import json
import pytest

meal_data_cases = [
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="Saved with soup",
        price=500), 404),
    (dict(
        category="BBQ Chicken",
        description="Saved with soup",
        price=500), 400),
    (dict(
        meal="Wali",
        description="Saved with soup",
        price=500), 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        price=500), 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="Saved with soup"), 400),
    (dict(
        meal=400,
        category="BBQ Chicken",
        description="Saved with soup",
        price=500), 400),
    (dict(
        meal="Wali",
        category=40,
        description="Saved with soup",
        price=500), 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="&%Saved with soup",
        price=500), 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="Saved with soup",
        price=0), 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="Saved with soup",
        price=500), 404),
    (dict(), 400),
    ("", 400)
]


@pytest.mark.parametrize("meal, status_code", meal_data_cases)
def test_create_meal(test_client, meal, status_code):
    "Function that tests different cases of creating meal with some data"
    response = test_client.post(
        "/api/v2/menu", data=json.dumps(meal),
        headers={"content-type": "application/json"})
    assert response.status_code == status_code


def test_get_available_meals(test_client):
    """Function that test availabily of meals"""
    response = test_client.get("/api/v2/menu")
    assert response.status_code == 404


def test_get_unavailable_meals(test_client):
    """Function that test unavailability of meals"""
    response = test_client.get("/api/v2/menu")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "meal_id, status_code", [
        (1, 404), ("a", 404)])
def test_get_specific_menu(test_client, meal_id, status_code):
    """Function that test requesting meal with deffent meal_ids"""
    response = test_client.get("/api/v2/menu/" + str(meal_id))
    assert response.status_code == status_code


def test_get_meals_with_invalid_url(test_client):
    """Function that test requecting meal without meal_id"""
    response = test_client.get("/api/v2/menu/")
    assert response.status_code == 404


def test_update_meals_with_invalid_url(test_client):
    "Function that tests update meal with invalid url"
    response = test_client.put("/api/v2/menu")
    assert response.status_code == 405


def test_update_meals_with_url_only(test_client):
    "Function that tests update meal with url only"
    response = test_client.put("/api/v2/menu/categories/")
    assert response.status_code == 404


update_cases = [
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="Saved with soup",
        price=500), 1, 404),
    (dict(
        category="BBQ Chicken",
        description="Saved with soup",
        price=500), 2, 400),
    (dict(
        meal="Wali",
        description="Saved with soup",
        price=500), 1, 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        price=500), 2, 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="Saved with soup"), 1, 400),
    (dict(
        meal=400,
        category="BBQ Chicken",
        description="Saved with soup",
        price=500), 3, 400),
    (dict(
        meal="Wali",
        category=40,
        description="Saved with soup",
        price=500), 1, 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="&%Saved with soup",
        price=500), 1, 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="Saved with soup",
        price=0), 1, 400),
    (dict(
        meal="Wali",
        category="BBQ Chicken",
        description="Saved with soup",
        price=500), 2, 404),
    (dict(), 1, 400),
    ("", 2, 400)
]


@pytest.mark.parametrize("meal, meal_id, status_code", update_cases)
def test_update_category(test_client, meal, meal_id, status_code):
    "Function that tests update meal with diffent cases"
    response = test_client.put(
        "/api/v2/menu/" + str(meal_id), data=json.dumps(meal),
        headers={"content-type": "application/json"})
    assert response.status_code == status_code


delete_cases = [
    (1, 404),
    (3000, 404),
    ("a", 404)
]


@pytest.mark.parametrize("meal_id, status_code", delete_cases)
def test_delete_meal(test_client, meal_id, status_code):
    "Function that tests delete meal with diffent cases"
    response = test_client.delete("/api/v2/menu/" + str(meal_id))
    assert response.status_code == status_code


def test_delete_meal_with_get_url(test_client):
    "Function that tests delete meal with url for get"
    response = test_client.delete("/api/v2/menu")
    assert response.status_code == 405


def test_delete_meal_without_meal_id(test_client):
    "Function that tests delete meal with url missing meal_id"
    response = test_client.delete("/api/v2/menu/")
    assert response.status_code == 404
