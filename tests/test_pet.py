from services.pet_service import create_pet, get_pet, delete_pet
import random


def test_create_and_get_pet():
    random_id = random.randint(1, 999999)
    payload = {
        "id": random_id,
        "name": "doggie",
        "status": "available"
    }

    #CREATE
    create_response = create_pet(payload)
    assert create_response.status_code == 200

    create_response_json = create_response.json()
    assert create_response_json["id"] == payload["id"]
    assert create_response_json["name"] == payload["name"]
    assert create_response_json["status"] == payload["status"]

    pet_id = create_response_json["id"]

    #GET
    get_pet_response = get_pet(pet_id)

    assert get_pet_response.status_code == 200

    get_pet_response_json = get_pet_response.json()
    assert get_pet_response_json["id"] == payload["id"]
    assert get_pet_response_json["name"] == payload["name"]
    assert get_pet_response_json["status"] == payload["status"]

    #DELETE
    delete_pet_response = delete_pet(pet_id)
    assert delete_pet_response.status_code == 200

    #VERIFY DELETE
    get_after_delete = get_pet(pet_id)
    assert get_after_delete.status_code == 404

