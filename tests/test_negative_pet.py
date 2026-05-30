import pytest
import allure

from utils.allure_utils import log_response


@pytest.mark.parametrize(
    "pet_id",
    [
            99999999,
        -1,
        0,
        "string"
    ]
)
def test_get_pet_negative_pet(pet_client, pet_id):
    with allure.step(f"GET pet with invalid id: {pet_id}"):
        response = pet_client.get_pet(pet_id)

        log_response(response)

    assert response.status_code != 200

@pytest.mark.parametrize(
    "pet_id",
    [
        99999999,
        -1,
        0,
        "string"
    ]
)
def test_delete_pet_negative(pet_client, pet_id):
    with allure.step(f"DELETE pet with invalid id: {pet_id}"):
        response = pet_client.delete_pet(pet_id)

        log_response(response)

    assert response.status_code != 200

@pytest.mark.parametrize(
    "payload, expected_status",
    [
        (
                {}, [400, 422]
         ),
        (
                {
                    "id": "string",
                    "name": "",
                    "status": False
                },
            [400, 422]
        ),
        (
                {
                    "id": -1,
                    "name": "",
                    "status": "invalid"
                },
            [400, 422, 500]
        )

    ]
)
@pytest.mark.xfail(

    reason="Swagger Petstore accepts invalid payloads inconsistently"

)
def test_create_pet_negative(pet_client, payload, expected_status):
    with allure.step(f"POST pet with invalid payload: {payload}"):
        response = pet_client.create_pet(payload)

        log_response(response)

    assert response.status_code in expected_status
    # API allows empty payload creation — behavior is inconsistent