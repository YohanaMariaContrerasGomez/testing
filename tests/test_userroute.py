import json


def test_create_user(client):
    data = {"email": "testuser2@test.com", "password": "testuser1"}

    response = client.post("/users", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser2@test.com"
    assert response.json()["is_active"] == True
