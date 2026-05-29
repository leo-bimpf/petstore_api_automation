from clients.base_client import BaseClient

class UserClient(BaseClient):
    def create_user(self, payload):
        return self.post("/user", json=payload)

    def get_user(self, username):
        return self.get(f"/user/{username}")

    def delete_user(self, username):
        return self.delete(f"/user/{username}")

    def put_user(self, username, payload):
        return self.put(f"/user/{username}", json=payload)

    def login_user(self, username, password):
        return self.get("/user/login", params={
            "username": username, "password": password
        })

    def logout_user(self):
        return self.get("/user/logout")

