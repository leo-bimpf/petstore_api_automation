from utils.schema_validator import validate_schema
from schemas.user_schema import user_schema
from schemas.action_schema import user_action_schema
from utils.allure_utils import log_response
import allure


@allure.feature("User API")
@allure.story("Create user")
@allure.title("Create user with valid payload")
def test_create_user(user_client, user_payload):
    response = user_client.create_user(user_payload)
    log_response(response)
    assert response.status_code == 200

    validate_schema(response, user_action_schema)

@allure.feature("User API")
@allure.story("Get user")
@allure.title("Get user by username")
def test_get_user(user_client, created_user):
    payload, username = created_user
    response = user_client.get_user(username)
    log_response(response)

    validate_schema(response, user_schema)

    assert response.status_code == 200
    assert response.json()["id"] == payload["id"]
    assert response.json()["username"] == payload["username"]
    assert response.json()["firstName"] == payload["firstName"]
    assert response.json()["lastName"] == payload["lastName"]
    assert response.json()["email"] == payload["email"]
    assert response.json()["password"] == payload["password"]
    assert response.json()["phone"] == payload["phone"]
    assert response.json()["userStatus"] == payload["userStatus"]

@allure.feature("User API")
@allure.story("Delete user")
@allure.title("Delete user and verify removal")
def test_delete_user(user_client, created_user):
    _, username = created_user

    delete_response = user_client.delete_user(username)
    log_response(delete_response)
    assert delete_response.status_code == 200

    get_after_delete_user = user_client.get_user(username)
    assert get_after_delete_user.status_code == 404

@allure.feature("User API")
@allure.story("Update user")
@allure.title("Update user information")
def test_update_user(user_client, created_user):
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

    update_response = user_client.put_user(username, updated_body)

    log_response(update_response)

    assert update_response.status_code == 200

    validate_schema(update_response, user_action_schema)

    get_response = user_client.get_user(username)
    response_json = get_response.json()

    assert response_json == updated_body
    assert response_json["firstName"] == updated_body["firstName"]
    assert response_json["email"] == updated_body["email"]
    assert response_json["lastName"] == updated_body["lastName"]
    assert response_json["phone"] == updated_body["phone"]

@allure.feature("User API")
@allure.story("Login user")
@allure.title("Login user with valid credentials")
def test_login_user(user_client, created_user):
    payload, username = created_user
    login_response = user_client.login_user(username=username, password=payload["password"])

    log_response(login_response)

    assert login_response.status_code == 200
    assert "logged in user session" in login_response.text
    assert "X-Rate-Limit" in login_response.headers
    assert "X-Expires-After" in login_response.headers



@allure.feature("User API")
@allure.story("Logout user")
@allure.title("Logout current user")
def test_logout_user(user_client):
    logout_response = user_client.logout_user()

    log_response(logout_response)

    assert logout_response.status_code == 200
