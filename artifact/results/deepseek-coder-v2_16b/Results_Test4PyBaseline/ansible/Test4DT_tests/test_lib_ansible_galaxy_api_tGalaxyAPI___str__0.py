
# Module: ansible.galaxy.api
# test_galaxy_api.py
from ansible.galaxy.api import GalaxyAPI
import pytest

@pytest.fixture
def default_api():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')

@pytest.fixture
def api_with_auth():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', username='user', password='pass', clear_response_cache=True, no_cache=False)

@pytest.fixture
def api_with_token():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', token='your_token_here', available_api_versions={'v1': 'http://api.ansiblegalaxy.com/v1'})

@pytest.fixture
def api_without_certs():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', validate_certs=False)

@pytest.fixture
def api_low_priority():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', no_cache=True, priority=1.0)

# Test cases for default initialization
def test_default_initialization(default_api):
    assert default_api.galaxy == 'exampleGalaxy'
    assert default_api.name == 'exampleClient'
    assert default_api.api_server == 'https://api.ansiblegalaxy.com'
    assert default_api.validate_certs is True