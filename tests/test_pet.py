from clients.pet_client import PetClient
from utils.allure_utils import log_response
import allure
pet_client = PetClient()

@allure.feature("Pet API")
@allure.story("Create pet")
@allure.title("Create pet with valid payload")
def test_create_pet(pet_payload):
    response = pet_client.create_pet(pet_payload)
    allure.attach(
        str(response.request.url),
        name="Request URL",
        attachment_type=allure.attachment_type.TEXT
    )

    log_response(response)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == pet_payload["id"]
    assert data["name"] == pet_payload["name"]
    assert data["status"] == pet_payload["status"]

@allure.feature("Pet API")
@allure.story("Delete pet")
@allure.title("Delete pet and verify it is removed")
def test_delete_pet(pet_payload):
    create_response = pet_client.create_pet(pet_payload)
    pet_id = create_response.json()["id"]

    delete_response = pet_client.delete_pet(pet_id)
    allure.attach(
        str(delete_response.request.url),
        name="DELETE URL",
        attachment_type=allure.attachment_type.TEXT
    )

    log_response(delete_response)

    assert delete_response.status_code == 200

    get_after_delete = pet_client.get_pet(pet_id)

    print("\nGET AFTER DELETE:", get_after_delete.json())

    assert get_after_delete.status_code == 404

@allure.feature("Pet API")
@allure.story("Get pet")
@allure.title("Get created pet by id")

def test_get_pet(created_pet):
    payload, pet_id = created_pet

    response = pet_client.get_pet(pet_id)

    allure.attach(
        str(response.request.url),
        name="GET URL",
        attachment_type=allure.attachment_type.TEXT
    )

    log_response(response)

    assert response.status_code == 200
    assert response.json()["id"] == payload["id"]
    assert response.json()["name"] == payload["name"]
    assert response.json()["status"] == payload["status"]