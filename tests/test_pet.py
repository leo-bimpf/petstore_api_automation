from services.pet_service import create_pet, get_pet, delete_pet


def test_create_and_get_pet(pet_payload):

    #CREATE
    create_response = create_pet(pet_payload)
    assert create_response.status_code == 200

    create_response_json = create_response.json()
    assert create_response_json["id"] == pet_payload["id"]
    assert create_response_json["name"] == pet_payload["name"]
    assert create_response_json["status"] == pet_payload["status"]

    pet_id = create_response_json["id"]

    #GET
    get_pet_response = get_pet(pet_id)

    assert get_pet_response.status_code == 200

    get_pet_response_json = get_pet_response.json()
    assert get_pet_response_json["id"] == pet_payload["id"]
    assert get_pet_response_json["name"] == pet_payload["name"]
    assert get_pet_response_json["status"] == pet_payload["status"]

    #DELETE
    delete_pet_response = delete_pet(pet_id)
    assert delete_pet_response.status_code == 200

    #VERIFY DELETE
    get_after_delete = get_pet(pet_id)
    assert get_after_delete.status_code == 404

def test_get_pet(created_pet):
    payload, pet_id = created_pet

    response = get_pet(pet_id)
    assert response.status_code == 200
    assert response.json()["id"] == payload["id"]