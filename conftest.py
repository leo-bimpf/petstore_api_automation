import pytest
import random

from clients.pet_client import PetClient
from clients.user_client import UserClient


@pytest.fixture
def pet_payload():
    return {
        "id": random.randint(1, 999999),
        "name": f"Pet-{random.randint(1, 999999)}",
        "status": "available",
    }

@pytest.fixture
def created_pet(pet_client, pet_payload):
    response = pet_client.create_pet(pet_payload)
    pet_id = response.json()["id"]

    yield pet_payload, pet_id

    pet_client.delete_pet(pet_id)

@pytest.fixture
def user_payload():
    user_id = random.randint(1, 999999)
    return {
        "id": user_id,
        "username": f"user{user_id}",
        "firstName": "John",
        "lastName": "Doe",
        "email": f"user{user_id}@test.com",
        "password": "pass123",
        "phone": f"+79{random.randint(100000000, 999999999)}",
        "userStatus": random.choice([0, 1])
    }

@pytest.fixture
def created_user(user_client, user_payload):
    response = user_client.create_user(user_payload)
    username = user_payload["username"]

    yield user_payload, username

    user_client.delete_user(username)

@pytest.fixture
def user_client():
    return UserClient()

@pytest.fixture
def pet_client():
    return PetClient()