
import pytest
from unittest.mock import patch
import requests
from httpie.models import HTTPRequest

def test_invalid_input():
    with patch('requests.Request.__init__', return_value=None):
        req = requests.Request('GET', 'http://example.com')
        http_req = HTTPRequest(req)
        http_req._orig.body = 123
        
        with pytest.raises(TypeError):
            http_req.body()
