
import pytest
from ansible.galaxy.api import GalaxyAPI

def test_default_initialization():
    api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
    assert isinstance(api_client, GalaxyAPI)
    assert api_client.galaxy == 'default_galaxy'
    assert api_client.name == 'default_name'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True

def test_authentication_with_username_and_password():
    api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', username='user123', password='pass123')
    assert isinstance(api_client, GalaxyAPI)
    assert api_client.galaxy == 'specific_galaxy'
    assert api_client.name == 'username123'
    assert api_client.username == 'user123'
    assert api_client.password == 'pass123'
    assert api_client.api_server == 'https://specific-server.com'
    assert api_client.validate_certs is True

def test_authentication_with_token():
    api_client = GalaxyAPI('specific_galaxy', 'token123', 'https://specific-server.com', token='abc123')
    assert isinstance(api_client, GalaxyAPI)
    assert api_client.galaxy == 'specific_galaxy'
    assert api_client.name == 'token123'
    assert api_client.token == 'abc123'
    assert api_client.api_server == 'https://specific-server.com'
    assert api_client.validate_certs is True

def test_disabling_tls_validation():
    api_client = GalaxyAPI('specific_galaxy', 'token123', 'https://specific-server.com', token='abc123', validate_certs=False)
    assert isinstance(api_client, GalaxyAPI)
    assert api_client.validate_certs is False

def test_disabling_cache():
    api_client = GalaxyAPI('example_galaxy', 'example_name', 'https://galaxy.ansible.com', no_cache=True)
    assert isinstance(api_client, GalaxyAPI)
    assert api_client._cache is None

def test_setting_priority():
    api_client = GalaxyAPI('example_galaxy', 'example_name', 'https://galaxy.ansible.com', priority=10)
    assert isinstance(api_client, GalaxyAPI)
    assert api_client._priority == 10
