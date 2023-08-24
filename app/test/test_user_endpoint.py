from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_create_user():
    data = {
        "username": "new_user",
        "password": "password123",
        "fullname": "New User",
        "designation": "1",
        "contact": "1234567890",
        "account_type": "0",
    }
    response = client.post("/api/users", json=data)
    assert response.status_code == 200
    assert response.json()["username"] == "new_user"


def test_get_all_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_one_user():
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "new_user"


def test_update_user():
    data = {
        "username": "updated_user",
        "password": "new_password",
        "fullname": "Updated User",
        "designation": "1",
        "contact": "9876543210",
        "account_type": "1",
    }
    response = client.put("/api/users/1", json=data)
    assert response.status_code == 202
    assert response.json()["username"] == "updated_user"
