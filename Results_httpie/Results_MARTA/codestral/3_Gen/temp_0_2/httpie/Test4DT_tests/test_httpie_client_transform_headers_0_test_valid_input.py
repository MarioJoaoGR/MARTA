
import pytest
from unittest.mock import patch
from httpie.client import transform_headers, IGNORE_CONTENT_LENGTH_METHODS
import requests

@pytest.fixture(autouse=True)
def setup():
    request = requests.Request('GET', 'http://example.com')
    prepared_request = request.prepare()
    prepared_request.headers['Content-Length'] = '0'
    return request, prepared_request

@pytest.mark.parametrize("method", ["GET", "POST", "PUT", "DELETE"])
def test_valid_input(setup, method):
    request, prepared_request = setup
    request.method = method
    with patch('httpie.client.IGNORE_CONTENT_LENGTH_METHODS', new={}):
        transform_headers(request, prepared_request)
        if method in IGNORE_CONTENT_LENGTH_METHODS:
            assert 'Content-Length' not in prepared_request.headers
        else:
            assert 'Content-Length' in prepared_request.headers
