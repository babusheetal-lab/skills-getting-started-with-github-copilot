from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_student_cannot_sign_up_twice():
    response = client.post(
        "/activities/Chess%20Club/signup?email=daniel@mergington.edu"
    )

    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_student_can_be_removed_from_activity():
    response = client.delete(
        "/activities/Chess%20Club/unregister?email=daniel@mergington.edu"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "daniel@mergington.edu removed from Chess Club"

    remaining = client.get("/activities")
    assert "daniel@mergington.edu" not in remaining.json()["Chess Club"]["participants"]
