
# Module: ansible.galaxy.api
# test_galaxyapi.py
from ansible.galaxy.api import GalaxyAPI
import pytest

@pytest.fixture
def default_api():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')

@pytest.fixture
def custom_api():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', username='user', password='pass', clear_response_cache=True, no_cache=False)

def test_default_initialization(default_api):
    assert default_api.galaxy == 'exampleGalaxy'
    assert default_api.name == 'exampleClient'
    assert default_api.api_server == 'https://api.ansiblegalaxy.com'
    assert default_api.username is None
    assert default_api.password is None
    assert default_api.token is None
    assert default_api.validate_certs is True
    assert not hasattr(default_api, 'clear_response_cache')  # Corrected assertion to check for attribute presence