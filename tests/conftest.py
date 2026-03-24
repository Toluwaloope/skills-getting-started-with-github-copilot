import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture
def sample_activity_name():
    return "Basketball"


@pytest.fixture
def sample_email():
    return "test.student@mergington.edu"


@pytest.fixture(autouse=True)
def reset_activities_state():
    original_state = copy.deepcopy(app_module.activities)
    try:
        yield
    finally:
        app_module.activities.clear()
        app_module.activities.update(copy.deepcopy(original_state))
