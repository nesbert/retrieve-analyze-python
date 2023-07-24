import requests

from gorest import BASE_URL, READ_TIMEOUT

resource_url = f"{BASE_URL}/v1/users"


def fetch(user_id: int):
    response = requests.get(f"{resource_url}/{user_id}", timeout=READ_TIMEOUT)
    response.raise_for_status()
    return response.json()


def fetch_all():
    response = requests.get(resource_url, timeout=READ_TIMEOUT)
    response.raise_for_status()

    return response.json()
