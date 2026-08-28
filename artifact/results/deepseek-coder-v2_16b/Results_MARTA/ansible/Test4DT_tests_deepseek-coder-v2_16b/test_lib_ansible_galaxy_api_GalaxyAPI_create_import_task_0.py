
import pytest
from ansible.galaxy.api import GalaxyAPI

# Test initialization without authentication details
def test_init_without_auth():
    api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
    assert api_client.galaxy == 'default_galaxy'
    assert api_client.name == 'default_name'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.username is None
    assert api_client.password is None
    assert api_client.token is None
    assert api_client.validate_certs is True
    assert api_client._available_api_versions == {}
    assert api_client._priority == float('inf')

# Test initialization with username and password for basic authentication
def test_init_with_basic_auth():
    api_client = GalaxyAPI(
        galaxy='specific_galaxy', 
        name=None, 
        url='https://specific-server.com', 
        username='user123', 
        password='pass123'
    )
    assert api_client.username == 'user123'
    assert api_client.password == 'pass123'
    assert api_client.token is None

# Test initialization with a token for OAuth authentication
def test_init_with_oauth_auth():
    api_client = GalaxyAPI(
        galaxy='specific_galaxy', 
        name=None, 
        url='https://specific-server.com', 
        token='abc123'
    )
    assert api_client.token == 'abc123'
    assert api_client.username is None
    assert api_client.password is None

# Test initialization without validating TLS certificates
def test_init_without_tls_validation():
    api_client = GalaxyAPI(
        galaxy='specific_galaxy', 
        name=None, 
        url='https://specific-server.com', 
        username='user123', 
        password='pass123', 
        validate_certs=False
    )
    assert api_client.validate_certs is False

# Test initialization with specific available API versions
def test_init_with_specific_api_versions():
    api_client = GalaxyAPI(
        galaxy='specific_galaxy', 
        name=None, 
        url='https://specific-server.com', 
        username='user123', 
        password='pass123', 
        available_api_versions={'v1': 'https://api.ansiblegalaxy.com/v1'}
    )
    assert api_client._available_api_versions == {'v1': 'https://api.ansiblegalaxy.com/v1'}

# Test initialization without caching data
def test_init_without_cache():
    api_client = GalaxyAPI(
        galaxy='specific_galaxy', 
        name=None, 
        url='https://specific-server.com', 
        username='user123', 
        password='pass123', 
        no_cache=True
    )
    assert api_client._cache is None

# Test initialization and clearing the response cache

# Test initialization with a specific priority level
def test_init_with_specific_priority():
    api_client = GalaxyAPI(
        galaxy='specific_galaxy', 
        name=None, 
        url='https://specific-server.com', 
        username='user123', 
        password='pass123', 
        priority=0.5
    )
    assert api_client._priority == 0.5