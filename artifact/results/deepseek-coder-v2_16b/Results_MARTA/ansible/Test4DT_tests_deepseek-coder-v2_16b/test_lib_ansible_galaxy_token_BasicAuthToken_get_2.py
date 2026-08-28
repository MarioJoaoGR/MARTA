
import pytest
from ansible.galaxy.token import BasicAuthToken

# Test valid input with password
def test_valid_input_with_password():
    token_with_password = BasicAuthToken('user', 'pass')
    assert token_with_password.get() == "dXNlcjpwYXNz"  # Base64 encoded "user:pass"

# Test valid input without password
def test_valid_input_without_password():
    token_without_password = BasicAuthToken('user')
    assert token_without_password.get() == "dXNlcjo="  # Base64 encoded "user:"

# Test invalid input with None
def test_invalid_input_none():
    try:
        token_with_none = BasicAuthToken(None)
    except TypeError as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'username'"
