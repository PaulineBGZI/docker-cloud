import requests

BASE_URL = "http://proxy:80"


def test_api_accessible():
    response = requests.get(f"{BASE_URL}/api/", timeout=5)
    assert response.status_code == 200


def test_api_returns_json():
    response = requests.get(f"{BASE_URL}/api/", timeout=5)
    assert "application/json" in response.headers["Content-Type"]
    assert response.json() is not None
