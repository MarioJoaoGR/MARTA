
import pytest
from httpie.plugins.builtin import HTTPBasicAuth
import requests
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def mock_requests():
    with patch('httpie.plugins.builtin.requests') as mock_requests:
        yield mock_requests

def test_invalid_input():
    auth = HTTPBasicAuth('123', 'password')
    request = requests.PreparedRequest()
    
    # Test with invalid username type (non-string)
    with pytest.raises(TypeError):
        auth = HTTPBasicAuth(123, 'password')
        auth(request)
    
    # Test with invalid password type (non-string)
    with pytest.raises(TypeError):
        auth = HTTPBasicAuth('username', 123)
        auth(request)
