
import pytest
from ansible.galaxy.token import BasicAuthToken

# Test valid input with both username and password
def test_valid_input_with_password():
    token_with_password = BasicAuthToken('user', 'pass')
    assert token_with_password.get() == 'dXNlcjpwYXNz'  # Base64 encoded "user:pass"

# Test valid input without a password
def test_valid_input_without_password():
    token_without_password = BasicAuthToken('user')
    assert token_without_password.get() == 'dXNlcjo='  # Base64 encoded "user:"

# Test with invalid username (None)
def test_invalid_username():
    token_with_invalid_username = BasicAuthToken(None, 'pass')
    assert token_with_invalid_username.get() == None  # No token should be generated for an invalid username
