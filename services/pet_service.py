from urllib import response

import requests
from config.settings import BASE_URL, HEADERS

def get_pet(pet_id):
    return requests.get(
        f"{BASE_URL}/pet/{pet_id}", headers=HEADERS
    )

def create_pet(pet_id):
    return requests.post(
        f"{BASE_URL}/pet", headers=HEADERS, json=pet_id
    )

def delete_pet(pet_id):
    return requests.delete(
        f"{BASE_URL}/pet/{pet_id}", headers=HEADERS
    )