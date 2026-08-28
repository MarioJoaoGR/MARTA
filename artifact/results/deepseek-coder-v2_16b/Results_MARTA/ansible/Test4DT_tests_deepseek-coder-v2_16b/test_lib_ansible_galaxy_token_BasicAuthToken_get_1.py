
import pytest
from ansible.galaxy.token import BasicAuthToken

def test_valid_input_with_password():
    token = BasicAuthToken('user', 'pass')
    assert token.get() == "dXNlcjpwYXNz"  # This is the Base64 encoding of "user:pass"

def test_valid_input_without_password():
    token = BasicAuthToken('user')
    assert token.get() == "dXNlcjo="  # This is the Base64 encoding of "user:"
