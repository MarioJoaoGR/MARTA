
import pytest
from ansible.galaxy.token import BasicAuthToken

# Test initialization with only the required parameter (username)
def test_basicauthtoken_initialization_with_only_username():
    token = BasicAuthToken('testuser')
    assert token.username == 'testuser'