
import pytest
from ansible.module_utils.urls import Request
from urllib.error import HTTPError

def test_valid_get_request():
    r = Request()
    response = r.open('GET', 'http://httpbin.org/get')
    assert response is not None
    assert response.code == 200

def test_invalid_url():
    r = Request()
    with pytest.raises(HTTPError):
        r.open('GET', 'invalid-url')

def test_error_case():
    r = Request(headers="not a dict")
    with pytest.raises(ValueError):
        r.get('http://httpbin.org/get')
