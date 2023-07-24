import pytest
import requests
import requests_mock

from gorest import users_v2

RESOURCE_URL = "https://gorest.co.in/public/v2/users"


def test_fetch():
    with requests_mock.Mocker() as mocker:
        mock_response = {"data": {"id": 1, "name": "John"}}
        mocker.get(f"{RESOURCE_URL}/1", json=mock_response)

        response = users_v2.fetch(1)

        assert response == mock_response


def test_fetch_all():
    with requests_mock.Mocker() as mocker:
        mock_response = {"data": [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]}
        mocker.get(f"{RESOURCE_URL}?page=1&per_page=2", json=mock_response)

        response = users_v2.fetch_all(1, 2)

        assert response == mock_response


def test_fetch_raises_exception_for_http_error():
    with requests_mock.Mocker() as mocker:
        mocker.get(f"{RESOURCE_URL}/1", status_code=404)

        with pytest.raises(requests.exceptions.HTTPError):
            users_v2.fetch(1)


def test_fetch_all_raises_exception_for_http_error():
    with requests_mock.Mocker() as mocker:
        mocker.get(f"{RESOURCE_URL}?page=1&per_page=2", status_code=404)

        with pytest.raises(requests.exceptions.HTTPError):
            users_v2.fetch_all(1, 2)
