
import pytest
from ansible.galaxy.token import BasicAuthToken

# Test initialization with both username and password
def test_basicauthtoken_initialization_with_both():
    token = BasicAuthToken('user', 'pass')
    assert token.username == 'user'
    assert token.password == 'pass'

# Test initialization with only username
def test_basicauthtoken_initialization_with_only_username():
    token = BasicAuthToken('user')
    assert token.username == 'user'
    assert token.password is None

# Test generating the token
def test_generate_token():
    token = BasicAuthToken('user', 'pass')
    generated_token = token._encode_token('user', 'pass')
    assert token.get() == generated_token

# Test accessing headers for HTTP requests
def test_accessing_headers():
    token = BasicAuthToken('user', 'pass')
    headers = token.headers()
    expected_header = {'Authorization': f'Basic {token._encode_token("user", "pass")}'}
    assert headers == expected_header

# Test generating the token without initialization (should raise a TypeError)
def test_generate_token_without_initialization():
    with pytest.raises(TypeError):
        BasicAuthToken()
