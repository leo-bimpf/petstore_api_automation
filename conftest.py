import pytest
import random
from services.pet_service import create_pet, delete_pet

@pytest.fixture
def pet_payload():
    return {
        "id": random.randint(1, 999999),
        "name": f"Pet-{random.randint(1, 999999)}",
        "status": "available",
    }

@pytest.fixture
def created_pet():
    payload = pet_payload()
    response = create_pet(payload)
    pet_id = response.json()["id"]

    yield pet_id, payload

    delete_pet(pet_id)