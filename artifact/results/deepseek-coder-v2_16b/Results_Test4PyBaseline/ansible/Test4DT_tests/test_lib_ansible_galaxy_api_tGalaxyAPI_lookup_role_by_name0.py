# Module: ansible.galaxy.api
# test_galaxy_api.py
from ansible.galaxy.api import GalaxyAPI
import pytest

@pytest.fixture
def api_client():
    return GalaxyAPI(galaxy='main', name='ansible-api', url='https://galaxy.ansible.com')

def test_lookup_role_by_name_basic(api_client):
    role = api_client.lookup_role_by_name('someuser.somerolename')
    assert role is not None, "Expected to find a role but got None"
    assert isinstance(role, dict), f"Expected role to be a dictionary, but got {type(role)}"

def test_lookup_role_by_name_custom_settings(api_client):
    api_client = GalaxyAPI(galaxy='main', name='ansible-api', url='https://galaxy.ansible.com', username='user', password='pass', clear_response_cache=True, no_cache=False)
    role = api_client.lookup_role_by_name('someuser.somerolename')
    assert role is not None, "Expected to find a role but got None"
    assert isinstance(role, dict), f"Expected role to be a dictionary, but got {type(role)}"

def test_lookup_role_by_name_different_galaxy_instance(api_client):
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')
    role = api_client.lookup_role_by_name('someuser.somerolename')
    assert role is not None, "Expected to find a role but got None"
    assert isinstance(role, dict), f"Expected role to be a dictionary, but got {type(role)}"

def test_lookup_role_by_name_not_found(api_client):
    role = api_client.lookup_role_by_name('nonexistentuser.nonsexistrolename')
    assert role is None, "Expected to not find a role but got a result"
