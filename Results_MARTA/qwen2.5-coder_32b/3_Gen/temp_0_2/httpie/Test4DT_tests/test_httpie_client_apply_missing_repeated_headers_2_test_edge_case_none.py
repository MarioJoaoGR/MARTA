
import pytest
from httpie.client import HTTPHeadersDict, apply_missing_repeated_headers
import requests
from unittest.mock import patch

@pytest.fixture
def original_headers():
    return HTTPHeadersDict({'Content-Type': 'application/json', 'Accept': 'application/json'})

@pytest.fixture
def prepared_request():
    req = requests.PreparedRequest()
    req.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    return req

def test_apply_missing_repeated_headers(original_headers, prepared_request):
    with patch('httpie.client.HTTPHeadersDict') as mock_headers:
        # Mock the HTTPHeadersDict to avoid actual creation of headers dictionary
        mock_headers.return_value = original_headers
        
        apply_missing_repeated_headers(original_headers, prepared_request)
        
        assert prepared_request.headers == {'Content-Type': 'application/json', 'Accept': 'application/json'}
