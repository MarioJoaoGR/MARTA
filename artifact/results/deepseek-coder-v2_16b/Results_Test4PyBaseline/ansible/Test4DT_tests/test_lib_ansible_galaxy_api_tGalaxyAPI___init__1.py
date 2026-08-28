
import pytest
from ansible.galaxy.api import GalaxyAPI
import os
import tempfile

# Test initialization with default settings
def test_default_initialization():
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')
    assert api_client.galaxy == 'exampleGalaxy'
    assert api_client.name == 'exampleClient'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True

# Test initialization with custom parameters
def test_custom_initialization():
    username = 'testuser'
    password = 'testpass'
    token = 'testtoken'
    validate_certs = False
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', 
                            username=username, password=password, token=token, validate_certs=validate_certs)
    assert api_client.username == username
    assert api_client.password == password
    assert api_client.token == token
    assert api_client.validate_certs is False

# Test initialization with available API versions
def test_api_versions_initialization():
    available_api_versions = {'v1': 'https://api.ansiblegalaxy.com/v1'}
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', 
                            available_api_versions=available_api_versions)
    assert api_client._available_api_versions == available_api_versions

# Test initialization with clear cache flag set to True
def test_clear_cache():
    with tempfile.TemporaryDirectory() as tmpdir:
        b_cache_path = os.path.join(tmpdir, 'api.json')  # Corrected the join function usage
        api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', 
                                clear_response_cache=True)
        assert not os.path.exists(b_cache_path)

# Test initialization with no cache flag set to False
def test_no_cache():
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', 
                            no_cache=False)
    assert isinstance(api_client._cache, dict)

# Test initialization with priority set to a finite value
def test_priority_initialization():
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', 
                            priority=10)
    assert api_client._priority == 10
