import requests

class ReverbClient:
    def __init__(self, token):
        self.base_url = "https://api.reverb.com/api"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Accept-Version": "3.0",   # ✅ REQUIRED
            "Content-Type": "application/json"
        }

    def get(self, endpoint, params=None):
        r = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params
        )
        return self._handle(r)

    def post(self, endpoint, data=None):
        r = requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=data
        )
        return self._handle(r)

    def put(self, endpoint, data=None):
        r = requests.put(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=data
        )
        return self._handle(r)

    def _handle(self, r):
        if r.status_code == 403:
            return {"error": "❌ Missing OAuth scope for this action"}
        if r.status_code == 404:
            return {"error": "❌ Endpoint not found (check scope or API version)"}
        if r.status_code >= 400:
            return {"error": r.text}
        return r.json()
