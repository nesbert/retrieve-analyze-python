import requests

from gorest import BASE_URL

base_url_v1 = f'{BASE_URL}/v2/users'

def fetch(user_id):
    response = requests.get(f'{base_url_v1}/{user_id}')
    response.raise_for_status()
    return response.json()

def fetch_all():
    response = requests.get(base_url_v1)
    response.raise_for_status()
    return response.json()
