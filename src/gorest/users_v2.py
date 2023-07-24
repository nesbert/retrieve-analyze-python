import requests

from gorest import BASE_URL, READ_TIMEOUT

resource_url = f"{BASE_URL}/v2/users"


def fetch(user_id: int):
    response = requests.get(f"{resource_url}/{user_id}", timeout=READ_TIMEOUT)
    response.raise_for_status()
    return response.json()


def fetch_all(page: int = 1, limit: int = 10):
    query = {"page": page, "per_page": limit}
    response = requests.get(resource_url, params=query, timeout=READ_TIMEOUT)
    response.raise_for_status()
    return response.json()
