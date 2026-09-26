from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.delete("/activities/Chess Club/signup?email=michael@mergington.edu")

    assert response.status_code == 200
    payload = response.json()
    assert payload["message"] == "Unregistered michael@mergington.edu from Chess Club"

    activities = client.get("/activities").json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]

    # Restore state for the next test runs.
    client.post("/activities/Chess Club/signup?email=michael@mergington.edu")
