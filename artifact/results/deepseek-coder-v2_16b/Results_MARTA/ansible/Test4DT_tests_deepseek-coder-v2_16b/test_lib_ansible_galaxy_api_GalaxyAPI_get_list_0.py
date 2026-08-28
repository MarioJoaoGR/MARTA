
import pytest
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def api_client():
    return GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')

def test_basic_initialization(api_client):
    assert api_client.galaxy == 'default_galaxy'
    assert api_client.name == 'default_name'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True

def test_authentication_via_username_and_password(api_client):
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', username='user123', password='pass123')
    assert api_client.username == 'user123'
    assert api_client.password == 'pass123'
    assert api_client.validate_certs is True

def test_disabling_tls_certificate_validation(api_client):
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', username='user123', password='pass123', validate_certs=False)
    assert api_client.validate_certs is False

def test_using_token_for_authentication(api_client):
    api_client = GalaxyAPI('specific_galaxy', 'token123', 'https://specific-server.com', token='abc123')
    assert api_client.token == 'abc123'
    assert api_client.validate_certs is True


def test_specifying_available_api_versions(api_client):
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', username='user123', password='pass123', available_api_versions={'v1': '/api/v1'})
    assert api_client._available_api_versions == {'v1': '/api/v1'}


def test_setting_priority(api_client):
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', username='user123', password='pass123', priority=0)
    assert api_client._priority == 0
