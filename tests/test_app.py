from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_student_cannot_sign_up_twice():
    response = client.post(
        "/activities/Chess%20Club/signup?email=daniel@mergington.edu"
    )

    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()
