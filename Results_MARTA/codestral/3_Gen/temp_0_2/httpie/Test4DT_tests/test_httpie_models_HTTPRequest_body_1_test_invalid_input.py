
import pytest
from unittest.mock import patch
import requests
from httpie.models import HTTPRequest

def test_invalid_input():
    with patch('requests.Request', autospec=True) as mock_req:
        # Set up the mock request object
        mock_req.return_value = mock_req
        mock_req.body = 123
        
        http_req = HTTPRequest(mock_req)
        
        with pytest.raises(TypeError):
            http_req.body()
