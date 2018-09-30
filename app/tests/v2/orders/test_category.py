"""Module that create test cases for category"""

import json
import pytest

create_category_cases = [
    (dict(), 400),
    ("", 400),
    (dict(category=49), 400),
    (dict(category="$%BBQ"), 400),
    (dict(category="BBQ Chicken"), 200),
    (dict(category="BBQ Chicken"), 200)
]

@pytest.mark.parametrize("category, status_code", create_category_cases)
def test_create_category(test_client, category, status_code):
    "Function that tests different cases of creating category"
    response = test_client.post(
        "/api/v2/menu/categories",
        data=json.dumps(category),
        headers={"content-type": "application/json"}
        )
    response.status_code == status_code

def test_request_unexist_category(test_client):
    "Function that tests request unexist category"
    response = test_client.get("/api/v2/menu/categories")
    response.status_code = 404

def test_request_exist_category(test_client):
    "Function that tests request exist category"
    response = test_client.get("/api/v2/menu/category")
    response.status_code == 200

get_cases = [
    ("", 400),
    ("a", 404),
    (1, 200),
    (3000, 404)
]
@pytest.mark.parametrize("cat_id, status_code", get_cases)
def test_request_specific_category(test_client, cat_id, status_code):
    "Function that tests request specific category by id with diffent cases"
    response = test_client.get("api/v2/menu/categories/" + str(cat_id))
    response.status_code == status_code

def test_update_category_with_invalid_url(test_client):
    "Function that tests update category with invalid url"
    response = test_client.put("/api/v2/menu/categories")
    assert response.status_code == 405

def test_update_category_with_url_only(test_client):
    "Function that tests update category with url only"
    response = test_client.put("/api/v2/menu/categories/")
    assert response.status_code == 404

update_cases = [
    ("", dict(), 404),
    (1, "", 400),
    (1, dict(), 400),
    (2000, dict(category="BBQ"), 404),
    (1, dict(category="BBQ Firigisi"), 200),
    (1, dict(category="%BBQQ"), 400)
]
@pytest.mark.parametrize("cat_id, cat_name, status_code", update_cases)
def test_update_category(test_client, cat_id, cat_name, status_code):
    "Function that tests update category with diffent cases"
    response = test_client.put(
        "/api/v2/menu/categories/" + str(cat_id), data=json.dumps(cat_name),
        headers={"content-type": "application/json"})
    assert response.status_code == status_code

delete_cases = [
    (1, 404),
    (3000, 404),
    ("a", 404)
]
@pytest.mark.parametrize("cat_id, status_code", delete_cases)
def test_delete_category(test_client, cat_id, status_code):
    "Function that tests delete category with diffent cases"
    response = test_client.delete("/api/v2/menu/categories" + str(cat_id))
    assert response.status_code == status_code


def test_delete_category_invalid_url(test_client):
    "Function that tests delete category with url for get"
    response = test_client.delete("/api/v2/menu/categories")
    assert response.status_code == 405


def test_delete_order_invalid_url_again(test_client):
    "Function that tests delete category with url missing cat_id"
    response = test_client.delete("/api/v2/menu/categories/")
    assert response.status_code == 404