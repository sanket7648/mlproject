from fastapi.testclient import TestClient
from src.main import app
from src.services.database import get_db
from src.models.feedback import Feedback
from sqlalchemy.orm import Session

client = TestClient(app)

def test_submit_feedback():
    response = client.post("/feedback/submit", json={
        "user_id": 1,
        "product_id": 1,
        "rating": 5,
        "comments": "Great product!"
    })
    assert response.status_code == 201
    assert response.json() == {"message": "Feedback submitted successfully"}

def test_get_feedback():
    response = client.get("/feedback/1")
    assert response.status_code == 200
    assert "rating" in response.json()
    assert "comments" in response.json()

def test_feedback_validation():
    response = client.post("/feedback/submit", json={
        "user_id": 1,
        "product_id": 1,
        "rating": 6,  # Invalid rating
        "comments": "Great product!"
    })
    assert response.status_code == 422  # Unprocessable Entity

def test_feedback_not_found():
    response = client.get("/feedback/999")  # Non-existent feedback ID
    assert response.status_code == 404
    assert response.json() == {"detail": "Feedback not found"}