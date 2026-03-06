from urllib.parse import quote


def test_signup_for_activity_success(client):
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    response = client.post(
        f"/activities/{quote(activity)}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity}"}

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity]["participants"]
    assert email in participants



def test_signup_for_activity_rejects_duplicate_email(client):
    activity = "Chess Club"
    existing_email = "michael@mergington.edu"

    response = client.post(
        f"/activities/{quote(activity)}/signup",
        params={"email": existing_email},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"



def test_signup_for_unknown_activity_returns_404(client):
    response = client.post(
        f"/activities/{quote('Unknown Club')}/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
