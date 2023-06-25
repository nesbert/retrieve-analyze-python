import requests
from gorest import BASE_URL

base_url_v1 = f'{BASE_URL}/v1/users'

def fetch(user_id):
    url = f'{base_url_v1}/{user_id}'

    print(f'Fetching user #{user_id} from {url}')

    response = requests.get(url)
    response.raise_for_status()

    return response.json()

def fetch_all():
    print(f'Fetching all users from {base_url_v1}')

    response = requests.get(base_url_v1)
    response.raise_for_status()

    return response.json()
