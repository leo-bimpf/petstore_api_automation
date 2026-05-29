import pytest
from clients.pet_client import PetClient
pet_client = PetClient()

@pytest.mark.parametrize(
    "pet_id",
    [
            99999999,
        -1,
        0,
        "string"
    ]
)
def test_get_pet_negative_pet(pet_id):
    response = pet_client.get_pet(pet_id)
    print("\nGET NEGATIVE:", response.text)
    assert response.status_code in [404, 400]

@pytest.mark.parametrize(
    "pet_id",
    [
        99999999,
        -1,
        0,
        "string"
    ]
)
def test_delete_pet_negative(pet_id):
    response = pet_client.delete_pet(pet_id)
    print("\nDELETE NEGATIVE:", response.text)
    assert response.status_code in [404, 400]

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
def test_create_pet_negative(payload, expected_status):
    response = pet_client.create_pet(payload)
    print("\nCREATE NEGATIVE:", response.json())
    assert response.status_code in expected_status
    # API allows empty payload creation — behavior is inconsistent