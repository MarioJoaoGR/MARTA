
import pytest
from unittest.mock import patch
from httpie.client import transform_headers, IGNORE_CONTENT_LENGTH_METHODS, apply_missing_repeated_headers
import requests

@pytest.fixture(autouse=True)
def setup():
    request = requests.Request('GET', 'http://example.com')
    prepared_request = request.prepare()
    prepared_request.headers['Content-Length'] = '0'
    return request, prepared_request

@patch('httpie.client.IGNORE_CONTENT_LENGTH_METHODS', {'GET'})
def test_valid_input(setup):
    request, prepared_request = setup
    transform_headers(request, prepared_request)
    assert 'Content-Length' not in prepared_request.headers
