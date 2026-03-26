
import requests
from unittest.mock import MagicMock
import pytest

def _get_confirm_token(resp):
    for key, value in resp.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

@pytest.fixture
def missing_cookie_response():
    response = requests.Response()
    response.cookies = MagicMock()
    response.cookies.get.return_value = None
    return response

def test_missing_cookie(missing_cookie_response):
    assert _get_confirm_token(missing_cookie_response) is None
