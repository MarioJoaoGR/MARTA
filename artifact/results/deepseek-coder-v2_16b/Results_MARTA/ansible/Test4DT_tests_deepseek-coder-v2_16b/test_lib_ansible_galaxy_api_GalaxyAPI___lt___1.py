
import pytest
from ansible.galaxy.api import GalaxyAPI

def test_default_initialization():
    api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
    assert isinstance(api_client, GalaxyAPI)

def test_authentication_with_username_and_password():
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', username='user123', password='pass123')
    assert api_client.username == 'user123'
    assert api_client.password == 'pass123'

def test_authentication_with_token():
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', token='token123')
    assert api_client.token == 'token123'

def test_disabling_tls_certificate_validation():
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', validate_certs=False)
    assert not api_client.validate_certs

def test_specifying_available_api_versions():
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', available_api_versions={'roles': 'v1'})
    assert api_client._available_api_versions == {'roles': 'v1'}


def test_disabling_cache():
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', no_cache=True)
    assert api_client._cache is None

def test_specifying_priority():
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', priority=0)
    assert api_client._priority == 0

def test_incorrect_argument_types():
    with pytest.raises(TypeError):
        GalaxyAPI()