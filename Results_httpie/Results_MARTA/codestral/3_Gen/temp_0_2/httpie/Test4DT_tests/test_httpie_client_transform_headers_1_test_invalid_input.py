
import requests
from unittest.mock import patch
from httpie.client import transform_headers

def test_invalid_input():
    with patch('requests.Request') as mock_request, \
         patch('requests.PreparedRequest') as mock_prepared_request:
        
        # Set up the mocks
        mock_request.return_value = requests.Request()
        mock_prepared_request.return_value = requests.PreparedRequest()
        
        # Call the function under test
        transform_headers(mock_request.return_value, mock_prepared_request.return_value)
        
        # Assert that 'Content-Length' is not in headers (as it should be removed if present)
        assert 'Content-Length' not in mock_prepared_request.return_value.headers
