
import pytest
from ansible.galaxy.api import GalaxyAPI
from unittest.mock import patch

def test_valid_input():
    api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
    assert api_client.galaxy == 'default_galaxy'
    assert api_client.name == 'default_name'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True

def test_edge_case():
    api_client = GalaxyAPI(None, None, None)
    assert api_client.galaxy is None
    assert api_client.name is None
    assert api_client.api_server is None
    assert api_client.validate_certs is True

def test_invalid_input():
    with pytest.raises(Exception):
        api_client = GalaxyAPI('nonexistent_galaxy', 'nonexistent_user', 'https://nonexistent.com/api')
