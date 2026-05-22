
import pytest
from httpie.plugins.builtin import HTTPBasicAuth
import requests
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def setup_auth():
    auth = HTTPBasicAuth('username', 'password')
    return auth

@pytest.mark.parametrize("invalid_input", [123, None, b'bytes'])
def test_invalid_input(setup_auth, invalid_input):
    with patch('httpie.plugins.builtin.HTTPBasicAuth.__init__', return_value=None):
        with pytest.raises(TypeError):
            setup_auth(requests.PreparedRequest())
