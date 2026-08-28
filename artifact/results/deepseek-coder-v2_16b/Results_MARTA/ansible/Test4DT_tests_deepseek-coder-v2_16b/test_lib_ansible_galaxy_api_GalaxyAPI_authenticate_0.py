
import pytest
from ansible.galaxy.api import GalaxyAPI

def test_valid_initialization():
    api = GalaxyAPI('test_galaxy', 'test_name', 'https://example.com')
    assert isinstance(api, GalaxyAPI)
    assert api.galaxy == 'test_galaxy'
    assert api.name == 'test_name'
    assert api.api_server == 'https://example.com'

def test_invalid_initialization():
    with pytest.raises(TypeError):
        GalaxyAPI()


def test_authenticate_invalid_token(monkeypatch):
    class MockResponse:
        def __init__(self, content):
            self.content = content
    
    monkeypatch.setattr('ansible.galaxy.api.open_url', lambda url, data, validate_certs, method, http_agent: MockResponse({'error': 'invalid token'}))
    
    api = GalaxyAPI('test_galaxy', 'test_name', 'https://example.com')
    with pytest.raises(Exception):
        api.authenticate('invalid_github_token')