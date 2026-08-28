
import pytest
from ansible.galaxy.api import GalaxyAPI
import os

@pytest.fixture
def api_client():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')

def test_default_initialization(api_client):
    assert api_client.galaxy == 'exampleGalaxy'
    assert api_client.name == 'exampleClient'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True
    assert not hasattr(api_client, 'username')  # Ensure username and password are optional
    assert not hasattr(api_client, 'password')  # Ensure username and password are optional
    assert api_client._priority == float('inf')

def test_custom_initialization():
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', username='user', password='pass', clear_response_cache=True, no_cache=False)
    assert api_client.galaxy == 'exampleGalaxy'
    assert api_client.name == 'exampleClient'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True
    assert api_client.username == 'user'
    assert api_client.password == 'pass'
    assert api_client._priority == float('inf')
    assert not os.path.exists(api_client._b_cache_path)  # Ensure cache is cleared if clear_response_cache is True

def test_remove_secret(api_client):
    with pytest.raises(AttributeError):
        api_client.remove_secret('12345')  # This should raise an error because the method is not implemented correctly in the fixture setup
