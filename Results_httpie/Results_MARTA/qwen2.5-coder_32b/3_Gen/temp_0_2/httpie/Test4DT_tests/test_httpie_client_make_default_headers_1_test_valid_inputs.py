
import argparse
from httpie.client import make_default_headers, HTTPHeadersDict
from unittest.mock import patch

def test_valid_inputs():
    # Create a namespace object to simulate command-line arguments
    args = argparse.Namespace(json=True, data=False, form=False, files=False)
    
    with patch('httpie.client.DEFAULT_UA', 'TestUserAgent'):
        with patch('httpie.client.JSON_ACCEPT', 'application/json'):
            with patch('httpie.client.JSON_CONTENT_TYPE', 'application/json'):
                headers = make_default_headers(args)
                
                assert isinstance(headers, HTTPHeadersDict), "Expected an instance of HTTPHeadersDict"
                assert headers['User-Agent'] == 'TestUserAgent', "Unexpected User-Agent header value"
                assert headers.get('Accept') == 'application/json', "Unexpected Accept header value"
                assert headers.get('Content-Type') == 'application/json', "Unexpected Content-Type header value"
