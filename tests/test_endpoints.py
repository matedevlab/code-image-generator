import base64
import pytest
from application.app import app, PLACEHOLDER_CODE
from flask import url_for
from pygments.styles import get_all_styles
from bs4 import BeautifulSoup
from unittest.mock import patch


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# Test Home Page Load:
# Scenario: Access the home page.
# Expected: Status code 200 and session contains PLACEHOLDER_CODE.


def test_home_page_load(client):
    response = client.get("/")
    assert response.status_code == 200
    with client.session_transaction() as session:
        assert session.get("code") == PLACEHOLDER_CODE


# Test Home Page Content:
# Scenario: Check home page's content.
# Expected: print('Hello, World!') within a <textarea> element in the HTML response.


def test_home_page_content(client):
    response = client.get("/")
    assert response.status_code == 200

    soup = BeautifulSoup(response.get_data(as_text=True), "html.parser")
    textarea_content = soup.find("textarea", {"class": "code"}).text.strip()

    assert "print('Hello, World!')" in textarea_content


# Test Save Code Functionality:
# Scenario: Post new code to /save_code.
# Expected: Redirect to home page, session updated with new code.


def test_save_code_functionality(client):
    new_code = "print('New code')"
    response = client.post("/save_code", data={"code": new_code}, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == url_for("code")

    # Check if the session is updated with the new code
    with client.session_transaction() as session:
        assert session.get("code") == new_code


# Test Reset Session Functionality:
# Scenario: Post request to /reset_session.
# Expected: Redirect to home page, session reset to default values.


def test_reset_session_functionality(client):
    # Set session data before resetting
    with client.session_transaction() as session:
        session["code"] = "print('Hello, Tests!')"
        session["style"] = "monokai"

    response = client.post("/reset_session", follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == url_for("code")

    # Check if the session has been reset to default values
    with client.session_transaction() as session:
        assert session.get("code") == PLACEHOLDER_CODE  # Default code
        assert session.get("style") is None  # Default style is None or default value


# Test Style Page Load:
# Scenario: Access the /style endpoint.
# Expected: Status code 200 and default style is set in the session.


def test_style_page_load(client):
    with client.session_transaction() as session:
        session["code"] = "print('Hello, World!')"

    # Check if the default style is set
    response = client.get("/style")
    assert response.status_code == 200
    with client.session_transaction() as session:
        assert session.get("style") == "default"


# Test All Styles Are Listed:
# Scenario: Check the style selection page content.
# Expected: All styles from get_all_styles() are listed.


def test_all_styles_are_listed(client):
    with client.session_transaction() as session:
        session["code"] = "print('Hello, World!')"

    response = client.get("/style")
    assert response.status_code == 200

    soup = BeautifulSoup(response.get_data(as_text=True), "html.parser")
    style_options = {option.text.strip() for option in soup.find_all("option")}

    # Get all styles from pygments
    expected_styles = set(get_all_styles())

    assert expected_styles.issubset(style_options)


# Test Style Selection Save:
# Scenario: Post a new style to /save_style.
# Expected: Redirect to style page, session updated with new style.


def test_style_selection_save(client):
    with client.session_transaction() as session:
        session["code"] = "print('Hello, World!')"

    new_style = "monokai"
    response = client.post(
        "/save_style", data={"style": new_style}, follow_redirects=True
    )
    assert response.status_code == 200
    assert response.request.path == url_for("style")

    # Check if the session is updated with the new style
    with client.session_transaction() as session:
        assert session.get("style") == new_style


# Test Error Handling in Image Generation:
# Scenario: Trigger an error in take_screenshot_from_url.
# Expected: /image endpoint responds with status code 500.


def test_image_route_error_handling(client):
    with patch("application.app.take_screenshot_from_url") as mock_take_screenshot:
        # Mock the screenshot function to raise an exception
        mock_take_screenshot.side_effect = Exception("Error generating image")

        response = client.get("/image")
        assert response.status_code == 500
