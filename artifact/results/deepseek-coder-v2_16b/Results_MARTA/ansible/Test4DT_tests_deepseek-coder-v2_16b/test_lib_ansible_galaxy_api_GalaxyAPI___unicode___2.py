
import pytest
from ansible.galaxy.api import GalaxyAPI

# Test initialization with default parameters
def test_default_initialization():
    api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
    assert isinstance(api_client, GalaxyAPI)
    assert api_client.galaxy == 'default_galaxy'
    assert api_client.name == 'default_name'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True

# Test initialization with authentication details and TLS certificate validation disabled
def test_initialization_with_auth_and_tls_disabled():
    api_client = GalaxyAPI(
        galaxy='specific_galaxy', 
        name='username123', 
        url='https://specific-server.com', 
        username='user123', 
        password='pass123', 
        validate_certs=False
    )
    assert isinstance(api_client, GalaxyAPI)
    assert api_client.galaxy == 'specific_galaxy'
    assert api_client.username == 'user123'
    assert api_client.password == 'pass123'
    assert api_client.validate_certs is False

# Test initialization with all optional parameters

# Test invalid inputs should raise ValueError