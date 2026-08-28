
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
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', token='your_token_here')

@pytest.fixture
def api_without_cache():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', no_cache=True, priority=1.0)

# Test initialization with default settings
def test_default_initialization(default_api):
    assert default_api.galaxy == 'exampleGalaxy'
    assert default_api.name == 'exampleClient'
    assert default_api.api_server == 'https://api.ansiblegalaxy.com'
    assert default_api.username is None
    assert default_api.password is None
    assert default_api.token is None