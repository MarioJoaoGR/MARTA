
import pytest
from ansible.galaxy.token import BasicAuthToken

def test_invalid_input_none():
    with pytest.raises(TypeError):
        BasicAuthToken()  # This should raise a TypeError because username is required but not provided

def test_valid_input():
    token = BasicAuthToken('user', 'pass')
    assert token.get() == 'dXNlcjpwYXNz'  # The encoded string for "user:pass"

def test_valid_input_without_password():
    token = BasicAuthToken('user')
    assert token.get() == 'dXNlcjo='  # The encoded string for "user:"
