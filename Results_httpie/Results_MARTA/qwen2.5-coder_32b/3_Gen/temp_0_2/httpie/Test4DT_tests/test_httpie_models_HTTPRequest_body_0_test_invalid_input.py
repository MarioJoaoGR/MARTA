
import pytest
from unittest.mock import patch
import requests
from httpie.models import HTTPRequest

def test_invalid_input():
    with patch('requests.Request', autospec=True) as mock_req:
        # Create a mock request object with an invalid body type (int)
        mock_req.return_value = mock_req
        mock_req.body = 12345
        
        # Instantiate the HTTPRequest class with the mock request
        http_req = HTTPRequest(mock_req.return_value)
        
        # Assert that calling body() method raises a TypeError
        with pytest.raises(TypeError):
            http_req.body()
