import pytest
import random
from clients.pet_client import PetClient
from tests.test_pet import pet_client


@pytest.fixture
def pet_payload():
    return {
        "id": random.randint(1, 999999),
        "name": f"Pet-{random.randint(1, 999999)}",
        "status": "available",
    }

@pytest.fixture
def created_pet(pet_payload):
    response = pet_client.create_pet(pet_payload)
    pet_id = response.json()["id"]

    yield pet_payload, pet_id

    pet_client.delete_pet(pet_id)

