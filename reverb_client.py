import requests

class ReverbClient:
    def __init__(self, token):
        self.base_url = "https://api.reverb.com/api"
        self.token = token

    def _headers(self, version="3.0"):
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Accept-Version": version,
            "Content-Type": "application/json"
        }

    def get(self, endpoint, version="3.0", params=None):
        r = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self._headers(version),
            params=params
        )
        return self._handle(r)

    def _handle(self, r):
        if r.status_code == 403:
            return {"error": "❌ Missing OAuth scope"}
        if r.status_code == 404:
            return {"error": "❌ Endpoint does not exist"}
        if r.status_code >= 400:
            return {"error": r.text}
        return r.json()
