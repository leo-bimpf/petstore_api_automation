import allure
import pytest
from utils.schema_validator import validate_schema
from schemas.user_schema import user_schema
from schemas.action_schema import user_action_schema
from utils.allure_utils import log_response


# =========================
# CREATE USER
# =========================
@pytest.mark.user
@pytest.mark.positive
@allure.feature("User API")
@allure.story("Create user")
@allure.title("Create user with valid payload")
def test_create_user(user_client, user_payload):

    with allure.step("Send request to create user"):
        response = user_client.create_user(user_payload)

    with allure.step("Log response"):
        log_response(response)

    with allure.step("Check status code is 200"):
        assert response.status_code == 200

    with allure.step("Validate response schema"):
        validate_schema(response, user_action_schema)


# =========================
# GET USER
# =========================
@pytest.mark.user
@pytest.mark.positive
@allure.feature("User API")
@allure.story("Get user")
@allure.title("Get user by username")
def test_get_user(user_client, created_user):

    with allure.step("Send request to get user"):
        payload, username = created_user
        response = user_client.get_user(username)

    with allure.step("Log response"):
        log_response(response)

    with allure.step("Check status code is 200"):
        assert response.status_code == 200

    with allure.step("Validate response schema"):
        validate_schema(response, user_schema)

    with allure.step("Validate response body fields"):
        assert response.json()["id"] == payload["id"]
        assert response.json()["username"] == payload["username"]
        assert response.json()["firstName"] == payload["firstName"]
        assert response.json()["lastName"] == payload["lastName"]
        assert response.json()["email"] == payload["email"]
        assert response.json()["password"] == payload["password"]
        assert response.json()["phone"] == payload["phone"]
        assert response.json()["userStatus"] == payload["userStatus"]


# =========================
# DELETE USER
# =========================
@pytest.mark.user
@pytest.mark.positive
@allure.feature("User API")
@allure.story("Delete user")
@allure.title("Delete user and verify removal")
def test_delete_user(user_client, created_user):

    with allure.step("Send request to delete user"):
        _, username = created_user
        delete_response = user_client.delete_user(username)

    with allure.step("Log response"):
        log_response(delete_response)

    with allure.step("Check status code is 200"):
        assert delete_response.status_code == 200

    with allure.step("Verify user is deleted"):
        get_after_delete_user = user_client.get_user(username)
        assert get_after_delete_user.status_code == 404


# =========================
# UPDATE USER
# =========================
@pytest.mark.user
@pytest.mark.positive
@allure.feature("User API")
@allure.story("Update user")
@allure.title("Update user information")
def test_update_user(user_client, created_user):
    with allure.step("Prepare updated payload"):
        payload, username = created_user
        updated_body = {
            "id": payload["id"],
            "username": username,
            "firstName": "UpdatedName",
            "lastName": "UpdatedLastName",
            "email": "updated@test.com",
            "password": "12345",
            "phone": "123456789",
            "userStatus": 1
        }

    with allure.step("Send request to update user"):
        update_response = user_client.put_user(username, updated_body)

    with allure.step("Log response"):
        log_response(update_response)

    with allure.step("Check status code is 200"):
        assert update_response.status_code == 200

    with allure.step("Validate response schema"):
        validate_schema(update_response, user_action_schema)

    with allure.step("Get updated user"):
        get_response = user_client.get_user(username)
        response_json = get_response.json()

    with allure.step("validate updated data"):
        assert response_json == updated_body


# =========================
# LOGIN USER
# =========================
@pytest.mark.user
@pytest.mark.positive
@allure.feature("User API")
@allure.story("Login user")
@allure.title("Login user with valid credentials")
def test_login_user(user_client, created_user):

    with allure.step("Send request to login user"):
        payload, username = created_user
        login_response = user_client.login_user(username=username, password=payload["password"])

    with allure.step("Log_response"):
        log_response(login_response)

    with allure.step("Check status code is 200"):
        assert login_response.status_code == 200

    with allure.step("Validate login response content"):
        assert "logged in user session" in login_response.text
        assert "X-Rate-Limit" in login_response.headers
        assert "X-Expires-After" in login_response.headers


# =========================
# LOGOUT USER
# =========================
@pytest.mark.user
@pytest.mark.positive
@allure.feature("User API")
@allure.story("Logout user")
@allure.title("Logout current user")
def test_logout_user(user_client):

    with allure.step("Send request to logout user"):
        logout_response = user_client.logout_user()

    with allure.step("Log response"):
        log_response(logout_response)

    with allure.step("Check status code is 200"):
        assert logout_response.status_code == 200