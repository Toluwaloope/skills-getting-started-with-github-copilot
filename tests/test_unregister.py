def test_unregister_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"
    params = {"email": email}

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params=params)

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}



def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    unknown_activity = "Nonexistent Club"
    params = {"email": "student@mergington.edu"}

    # Act
    response = client.delete(f"/activities/{unknown_activity}/unregister", params=params)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}



def test_unregister_not_registered_student_returns_404(client):
    # Arrange
    activity_name = "Basketball"
    params = {"email": "student@mergington.edu"}

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params=params)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not registered for this activity"}



def test_unregister_removes_student_from_participants(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    params = {"email": email}

    # Act
    unregister_response = client.delete(
        f"/activities/{activity_name}/unregister",
        params=params,
    )

    # Assert
    assert unregister_response.status_code == 200
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email not in participants
