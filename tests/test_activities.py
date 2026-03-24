def test_get_activities_returns_seeded_data(client):
    # Arrange
    expected_activity_count = 9

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == expected_activity_count
    assert "Chess Club" in data
    assert "Programming Class" in data


def test_get_activities_items_have_expected_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    for activity in activities.values():
        assert required_fields.issubset(activity.keys())


def test_get_activities_includes_seed_participant(client):
    # Arrange
    expected_participant = "michael@mergington.edu"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert expected_participant in activities["Chess Club"]["participants"]
