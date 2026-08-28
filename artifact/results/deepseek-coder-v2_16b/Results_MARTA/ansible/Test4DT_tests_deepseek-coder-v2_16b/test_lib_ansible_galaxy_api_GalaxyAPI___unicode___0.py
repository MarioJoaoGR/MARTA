
import pytest
from ansible.galaxy.api import GalaxyAPI

def test_valid_inputs():
    api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
    assert isinstance(api_client, GalaxyAPI)
    assert api_client.galaxy == 'default_galaxy'
    assert api_client.name == 'default_name'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'

def test_edge_cases():
    with pytest.raises(ValueError):
        api_client = GalaxyAPI(None, None, 'invalid_url', validate_certs=False)

def test_invalid_inputs():
    with pytest.raises(TypeError):
        api_client = GalaxyAPI('', '', '')
