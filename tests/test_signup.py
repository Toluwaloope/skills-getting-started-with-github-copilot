def test_signup_success(client, sample_activity_name, sample_email):
    # Arrange
    params = {"email": sample_email}

    # Act
    response = client.post(f"/activities/{sample_activity_name}/signup", params=params)

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Signed up {sample_email} for {sample_activity_name}"
    }



def test_signup_duplicate_student_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    duplicate_email = "michael@mergington.edu"
    params = {"email": duplicate_email}

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params=params)

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up"}



def test_signup_unknown_activity_returns_404(client, sample_email):
    # Arrange
    unknown_activity = "Nonexistent Club"
    params = {"email": sample_email}

    # Act
    response = client.post(f"/activities/{unknown_activity}/signup", params=params)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}



def test_signup_adds_student_to_activity_participants(client, sample_activity_name, sample_email):
    # Arrange
    params = {"email": sample_email}

    # Act
    signup_response = client.post(
        f"/activities/{sample_activity_name}/signup",
        params=params,
    )

    # Assert
    assert signup_response.status_code == 200
    activities_response = client.get("/activities")
    participants = activities_response.json()[sample_activity_name]["participants"]
    assert sample_email in participants
