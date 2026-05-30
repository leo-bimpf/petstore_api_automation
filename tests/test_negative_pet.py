import pytest
import allure
from utils.allure_utils import log_response


# =========================
# GET PET NEGATIVE
# =========================
@allure.feature("Pet API")
@allure.story("Negative cases")
@allure.title("Get pet with invalid id")
@pytest.mark.parametrize(
    "pet_id",
    [99999999, -1, 0, "string"]
)
def test_get_pet_negative_pet(pet_client, pet_id):

    with allure.step(f"Send GET pet with invalid id: {pet_id}"):
        response = pet_client.get_pet(pet_id)

    with allure.step("Log response"):
        log_response(response)

    with allure.step("Check response status is NOT 200"):
        assert response.status_code != 200


# =========================
# DELETE PET NEGATIVE
# =========================
@allure.feature("Pet API")
@allure.story("Negative cases")
@allure.title("Delete pet with invalid id")
@pytest.mark.parametrize(
    "pet_id",
    [99999999, -1, 0, "string"]
)
def test_delete_pet_negative(pet_client, pet_id):

    with allure.step(f"DELETE pet with invalid id: {pet_id}"):
        response = pet_client.delete_pet(pet_id)

    with allure.step("Log response"):
        log_response(response)

    with allure.step("Check response status is NOT 200"):
        assert response.status_code != 200


# =========================
# CREATE PET NEGATIVE
# =========================
@allure.feature("Pet API")
@allure.story("Negative cases")
@allure.title("Create pet with invalid payload")
@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({}, [400, 422]),
        ({"id": "string", "name": "", "status": False},[400, 422] ),
        ({"id": -1, "name": "", "status": "invalid"},[400, 422, 500])

    ]
)
@pytest.mark.xfail(reason="Swagger Petstore accepts invalid payloads inconsistently")
def test_create_pet_negative(pet_client, payload, expected_status):

    with allure.step(f"POST pet with invalid payload: {payload}"):
        response = pet_client.create_pet(payload)

    with allure.step("Log response"):
        log_response(response)

    with allure.step(f"Check response status is in {expected_status}"):
        assert response.status_code in expected_status