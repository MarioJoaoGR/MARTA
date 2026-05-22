
import requests
from unittest.mock import patch
from httpie.client import transform_headers, apply_missing_repeated_headers, IGNORE_CONTENT_LENGTH_METHODS

def test_valid_input():
    request = requests.Request('GET', 'http://example.com')
    prepared_request = request.prepare()
    prepared_request.headers['Content-Length'] = '0'
    
    with patch('httpie.client.IGNORE_CONTENT_LENGTH_METHODS', {'GET'}):
        transform_headers(request, prepared_request)
        
        assert 'Content-Length' not in prepared_request.headers
