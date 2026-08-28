
import pytest
from ansible.galaxy.token import BasicAuthToken

# Test initialization with both username and password
def test_basicauthtoken_initialization_with_both():
    token = BasicAuthToken('testuser', 'testpass')
    assert token.username == 'testuser'
    assert token.password == 'testpass'
    assert token._token is None  # Check that _token is initialized to None

# Test initialization with only the required parameter (username)
def test_basicauthtoken_initialization_with_only_username():
    token = BasicAuthToken('testuser')
    assert token.username == 'testuser'
    assert token.password is None  # Check that password defaults to None