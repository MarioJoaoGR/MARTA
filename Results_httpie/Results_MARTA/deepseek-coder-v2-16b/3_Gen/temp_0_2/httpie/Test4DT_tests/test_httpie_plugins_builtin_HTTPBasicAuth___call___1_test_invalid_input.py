
import pytest
from httpie.plugins.builtin import HTTPBasicAuth
import requests
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup():
    auth = HTTPBasicAuth('username', 'password')
    request = requests.PreparedRequest()
    return auth, request

@pytest.mark.parametrize("invalid_input", [123, None, True, b'bytes'])
def test_invalid_input(setup, invalid_input):
    auth, request = setup
    with patch('httpie.plugins.builtin.HTTPBasicAuth.make_header', return_value='username:password'):
        if isinstance(invalid_input, str):
            auth.username = invalid_input
            auth.password = 'password'
            request = auth(request)
            assert 'Authorization' in request.headers
            assert request.headers['Authorization'] == b'Basic dXNlcm5hbWU6cGFzc3dvcmQ='
        else:
            with pytest.raises(TypeError):
                auth.username = invalid_input
                auth(request)
