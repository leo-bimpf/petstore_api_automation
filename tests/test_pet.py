from services.pet_service import create_pet, get_pet, delete_pet


def test_create_pet(pet_payload):
    response = create_pet(pet_payload)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == pet_payload["id"]
    assert data["name"] == pet_payload["name"]
    assert data["status"] == pet_payload["status"]


def test_delete_pet(pet_payload):
    create_response = create_pet(pet_payload)
    pet_id = create_response.json()["id"]

    delete_response = delete_pet(pet_id)
    assert delete_response.status_code == 200

    get_after_delete = get_pet(pet_id)
    assert get_after_delete.status_code == 404

def test_get_pet(created_pet):
    payload, pet_id = created_pet

    response = get_pet(pet_id)

    assert response.status_code == 200
    assert response.json()["id"] == payload["id"]
    assert response.json()["name"] == payload["name"]
    assert response.json()["status"] == payload["status"]