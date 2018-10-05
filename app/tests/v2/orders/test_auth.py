import json
import pytest

def test_user_auth(test_client):
    response = test_client.post("/api/v2/auth/signup", data=json.dumps(dict(user_name='semainda', password='semainda')))
    response.status_code == 200