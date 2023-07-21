import requests

from src.config import URL_COINDESK


def test_should_return_200():
    response = requests.get(URL_COINDESK)
    assert response.status_code == 200
