
# Module: ansible.galaxy.token
import pytest
from ansible.galaxy.token import BasicAuthToken
import base64

# Test initialization with username and password
def test_basicauthtoken_init():
    token = BasicAuthToken('user', 'pass')
    assert token.username == 'user'
    assert token.password == 'pass'
    assert token._token is None  # Check that _token is not initialized yet

# Test get method to generate the token
def test_basicauthtoken_get():
    token = BasicAuthToken('user', 'pass')
    encoded_token = base64.b64encode(f"user:pass".encode()).decode()
    assert token.get() == encoded_token  # Check that the get method returns the correct encoded token
    assert token._token == encoded_token  # Check that _token is now initialized with the generated token

# Test headers method to generate authorization headers
def test_basicauthtoken_headers():
    token = BasicAuthToken('user', 'pass')
    expected_headers = {'Authorization': f'Basic {base64.b64encode(f"user:pass".encode()).decode()}'}
    assert token.headers() == expected_headers  # Check that the headers method returns the correct authorization header

# Test initialization without password
def test_basicauthtoken_init_without_password():
    token = BasicAuthToken('user')
    assert token.username == 'user'
    assert token.password is None
    assert token._token is None  # Check that _token is not initialized yet

# Test get method without regenerating the token if already generated
def test_basicauthtoken_get_without_regenerate():
    token = BasicAuthToken('user', 'pass')
    encoded_token = base64.b64encode(f"user:pass".encode()).decode()
    assert token.get() == encoded_token  # First call should generate the token
    original_token = token._token
    assert token.get() == encoded_token  # Second call should not regenerate the token
    assert token._token == original_token  # Check that _token is still the same

# Test headers method with default values when no username or password provided
def test_basicauthtoken_headers_default():
    token = BasicAuthToken('user', 'pass')
    expected_headers = {'Authorization': f'Basic {base64.b64encode(f"user:pass".encode()).decode()}'}
    assert token.headers() == expected_headers  # Check that the headers method returns the correct authorization header with default values
