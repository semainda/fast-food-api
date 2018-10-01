"""Module that create test cases for meal"""

import json
import pytest

meal_data_cases = [
    (dict(meal="Wali", category="BBQ Chicken", description="Saved with soup", price=500), 404),
    (dict(category="BBQ Chicken", description="Saved with soup", price=500), 400),
    (dict(meal="Wali",description="Saved with soup", price=500), 400),
    (dict(meal="Wali", category="BBQ Chicken", price=500), 400),
    (dict(meal="Wali", category="BBQ Chicken", description="Saved with soup"), 400),
    (dict(meal=400, category="BBQ Chicken", description="Saved with soup", price=500), 400),
    (dict(meal="Wali", category=40, description="Saved with soup", price=500), 400),
    (dict(meal="Wali", category="BBQ Chicken", description="&%Saved with soup", price=500), 400),
    (dict(meal="Wali", category="BBQ Chicken", description="Saved with soup", price=0), 400),
    (dict(meal="Wali", category="BBQ Chicken", description="Saved with soup", price=500), 404),
    (dict(), 400),
    ("", 400)
]
@pytest.mark.parametrize("meal, status_code", meal_data_cases)
def test_create_meal(test_client, meal, status_code):
    "Function that tests different cases of creating meal with some data"
    response = test_client.post("/api/v2/menu", data=json.dumps(meal),
        headers={"content-type": "application/json"})
    assert response.status_code == status_code