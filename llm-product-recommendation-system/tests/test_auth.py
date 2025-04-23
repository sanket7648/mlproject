from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from src.api.auth import register_user, login_user
from src.models.user import User
from src.services.database import get_user_by_username, create_user

import sys
print("sys.path:", sys.path)

app = FastAPI()
client = TestClient(app)

@app.post("/register")
def test_register_user():
    response = client.post("/register", json={"username": "testuser", "password": "testpass", "email": "test@example.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "User registered successfully"}

    user = get_user_by_username("testuser")
    assert user is not None
    assert user.username == "testuser"

@app.post("/login")
def test_login_user():
    create_user(User(username="testuser", password_hash="hashed_testpass", email="test@example.com"))
    
    response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

    response = client.post("/login", json={"username": "testuser", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}