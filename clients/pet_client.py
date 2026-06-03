from clients.base_client import BaseClient
class PetClient(BaseClient):

    def create_pet(self, payload):
        return self.post("/pet", json=payload)

    def get_pet(self, pet_id):
        return self.get(f"/pet/{pet_id}")

    def delete_pet(self, pet_id):
        return self.delete(f"/pet/{pet_id}")

    def update_pet(self, payload):
        return self.put("/pet", json=payload)

    def find_by_status(self, status):
        return self.get("/pet/findByStatus", params={"status": status})
