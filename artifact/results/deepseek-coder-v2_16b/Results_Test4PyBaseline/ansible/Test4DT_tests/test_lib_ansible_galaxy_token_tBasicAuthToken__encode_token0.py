
import pytest
from ansible.galaxy.token import BasicAuthToken

# Test case for initializing a BasicAuthToken with both username and password
def test_basicauthtoken_with_username_and_password():
    token = BasicAuthToken('user', 'pass')
    assert token.username == 'user'
    assert token.password == 'pass'

# Test case for initializing a BasicAuthToken with only the username
def test_basicauthtoken_with_only_username():
    token = BasicAuthToken('user')
    assert token.username == 'user'