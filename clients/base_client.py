import requests

from config.settings import BASE_URL, HEADERS

class BaseClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def get(self,endpoint, params=None):
        return self.session.get(
            f"{self.base_url}{endpoint}", params=params
        )

    def post(self, endpoint, json=None):
        return self.session.post(
            f"{self.base_url}{endpoint}", json=json
        )

    def delete(self, endpoint):
        return self.session.delete(
            f"{self.base_url}{endpoint}"
        )

    def put(self, endpoint, json=None):
        return self.session.put(
            f"{self.base_url}{endpoint}", json=json
        )