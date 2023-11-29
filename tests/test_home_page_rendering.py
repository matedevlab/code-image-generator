import pytest
from application.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_home_page_renders_with_placeholder_code(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Paste Your Python Code" in response.data
    assert b"print('Hello, World!')" in response.data
