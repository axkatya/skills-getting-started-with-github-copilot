from urllib.parse import quote


def test_unregister_from_activity_success(client):
    activity = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{quote(activity)}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity}"}

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity]["participants"]
    assert email not in participants



def test_unregister_for_unknown_activity_returns_404(client):
    response = client.delete(
        f"/activities/{quote('Unknown Club')}/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"



def test_unregister_missing_participant_returns_404(client):
    activity = "Chess Club"
    response = client.delete(
        f"/activities/{quote(activity)}/signup",
        params={"email": "notregistered@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
