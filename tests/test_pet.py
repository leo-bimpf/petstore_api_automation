import allure
from utils.allure_utils import log_response
from utils.schema_validator import validate_schema
from schemas.pet_schema import pet_schema


# =========================
# CREATE PET
# =========================
@allure.feature("Pet API")
@allure.story("Create pet")
@allure.title("Create pet with valid payload")
def test_create_pet(pet_client, pet_payload):

    with allure.step("Send request to create pet"):
        response = pet_client.create_pet(pet_payload)

    with allure.step("Log response"):
        log_response(response)

    with allure.step("Check status code is 200"):
        assert response.status_code == 200

    with allure.step("Validate response schema"):
        validate_schema(response, pet_schema)

    with allure.step("Validate response body matches request"):
        data = response.json()
        assert data["id"] == pet_payload["id"]
        assert data["name"] == pet_payload["name"]
        assert data["status"] == pet_payload["status"]


# =========================
# DELETE PET
# =========================
@allure.feature("Pet API")
@allure.story("Delete pet")
@allure.title("Delete pet and verify it is removed")
def test_delete_pet(pet_client, pet_payload):

    with allure.step("Create pet for test precondition"):
        create_response = pet_client.create_pet(pet_payload)
        pet_id = create_response.json()["id"]

    with allure.step("Send request to delete pet"):
        delete_response = pet_client.delete_pet(pet_id)

    with allure.step("Log response"):
        log_response(delete_response)

    with allure.step("Check status code is 200"):
        assert delete_response.status_code == 200

    with allure.step("Verify pet is deleted (GET returns 404)"):
        get_after_delete = pet_client.get_pet(pet_id)
        assert get_after_delete.status_code == 404


# =========================
# GET PET
# =========================
@allure.feature("Pet API")
@allure.story("Get pet")
@allure.title("Get created pet by id")
def test_get_pet(pet_client, created_pet):
    with allure.step("Send request to get pet"):
        payload, pet_id = created_pet
        response = pet_client.get_pet(pet_id)

    with allure.step("Log response"):
        log_response(response)

    with allure.step("Check status code is 200"):
        assert response.status_code == 200

    with allure.step("Validate response schema"):
        validate_schema(response, pet_schema)

    with allure.step("Validate response data"):
        assert response.json()["id"] == payload["id"]
        assert response.json()["name"] == payload["name"]
        assert response.json()["status"] == payload["status"]