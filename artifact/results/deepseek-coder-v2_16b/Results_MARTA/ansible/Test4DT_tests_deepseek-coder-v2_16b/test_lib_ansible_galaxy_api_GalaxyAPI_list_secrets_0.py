
import pytest
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture(scope="module")
def api_client():
    return GalaxyAPI('example_galaxy', 'username123', 'https://specific-server.com', username='user123', password='pass123')

# Test initialization with basic authentication details
def test_init_with_basic_auth(api_client):
    assert api_client.name == 'username123'
    assert api_client.username == 'user123'
    assert api_client.password == 'pass123'
    assert api_client.validate_certs is True

# Test initialization without authentication details
def test_init_without_auth():
    api_client = GalaxyAPI('example_galaxy', 'username123', 'https://specific-server.com')
    assert api_client.name == 'username123'
    assert api_client.username is None
    assert api_client.password is None
    assert api_client.validate_certs is True

# Test initialization with token authentication and disabling TLS certificate validation
def test_init_with_token_auth():
    api_client = GalaxyAPI('example_galaxy', 'token123', 'https://specific-server.com', token='your_api_token', validate_certs=False)
    assert api_client.name == 'token123'
    assert api_client.token == 'your_api_token'
    assert api_client.validate_certs is False

# Test fetching a list of secrets from the API