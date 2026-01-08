import requests

class ReverbClient:
    def __init__(self, token):
        self.base_url = "https://api.reverb.com/api"
        self.token = token

    def _headers(self, version=None):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        # Only include Accept-Version when explicitly required
        if version:
            headers["Accept-Version"] = version

        return headers

    def get(self, endpoint, version=None, params=None):
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
