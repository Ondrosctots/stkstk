import requests

class ReverbClient:
    def __init__(self, token):
        self.base_url = "https://api.reverb.com/api"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get(self, endpoint, params=None):
        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params
        )
        return self._handle_response(response)

    def post(self, endpoint, data=None):
        response = requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=data
        )
        return self._handle_response(response)

    def put(self, endpoint, data=None):
        response = requests.put(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=data
        )
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 403:
            return {"error": "❌ Missing OAuth scope for this action"}
        if response.status_code >= 400:
            return {"error": response.text}
        return response.json()
