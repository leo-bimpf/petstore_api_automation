from clients.user_client import UserClient
from utils.allure_utils import log_response

import allure

user_client = UserClient()

@allure.feature("User API")
@allure.story("Create user")
@allure.title("Create user with valid payload")
def test_create_user(user_payload):
    response = user_client.create_user(user_payload)
    log_response(response)
    assert response.status_code == 200

@allure.feature("User API")
@allure.story("Get user")
@allure.title("Get user by username")
def test_get_user(created_user):
    payload, username = created_user
    response = user_client.get_user(username)
    log_response(response)

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
def test_delete_user(created_user):
    payload, username = created_user

    delete_response = user_client.delete_user(username)
    log_response(delete_response)
    assert delete_response.status_code == 200

    get_after_delete_user = user_client.get_user(username)
    assert get_after_delete_user.status_code == 404