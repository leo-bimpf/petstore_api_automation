from clients.pet_client import PetClient
pet_client = PetClient()

def test_create_pet(pet_payload):
    response = pet_client.create_pet(pet_payload)
    print("\nCREATE RESPONSE:", response.json())

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == pet_payload["id"]
    assert data["name"] == pet_payload["name"]
    assert data["status"] == pet_payload["status"]


def test_delete_pet(pet_payload):
    create_response = pet_client.create_pet(pet_payload)
    pet_id = create_response.json()["id"]

    delete_response = pet_client.delete_pet(pet_id)
    print("\nDELETE RESPONSE:", delete_response.json())

    assert delete_response.status_code == 200

    get_after_delete = pet_client.get_pet(pet_id)

    print("\nGET AFTER DELETE:", get_after_delete.json())

    assert get_after_delete.status_code == 404

def test_get_pet(created_pet):
    payload, pet_id = created_pet

    response = pet_client.get_pet(pet_id)

    print("\nGET RESPONSE:", response.json())

    assert response.status_code == 200
    assert response.json()["id"] == payload["id"]
    assert response.json()["name"] == payload["name"]
    assert response.json()["status"] == payload["status"]