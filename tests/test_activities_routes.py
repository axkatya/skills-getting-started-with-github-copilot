def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert payload



def test_get_activities_items_have_expected_shape(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()

    required_keys = {"description", "schedule", "max_participants", "participants"}

    for _, activity in payload.items():
        assert required_keys.issubset(activity.keys())
        assert isinstance(activity["participants"], list)
        assert isinstance(activity["max_participants"], int)
