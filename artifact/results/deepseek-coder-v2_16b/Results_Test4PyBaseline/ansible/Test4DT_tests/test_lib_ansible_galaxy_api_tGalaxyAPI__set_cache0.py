
# Module: ansible.galaxy.api
# test_galaxy_api.py
from ansible.galaxy.api import GalaxyAPI
import pytest
import os
import json

@pytest.fixture
def default_api():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')

@pytest.fixture
def api_with_auth():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', username='user', password='pass')

@pytest.fixture
def api_with_cache_clear():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', clear_response_cache=True)

@pytest.fixture
def api_without_cache():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', no_cache=True)

@pytest.fixture
def api_with_priority():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', priority=1.0)

@pytest.fixture
def api_with_token():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com', token='your_api_token')

@pytest.fixture
def api_with_all_params():
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

def test_initialization_with_auth(api_with_auth):
    assert api_with_auth.galaxy == 'exampleGalaxy'
    assert api_with_auth.name == 'exampleClient'
    assert api_with_auth.api_server == 'https://api.ansiblegalaxy.com'
    assert api_with_auth.username == 'user'
    assert api_with_auth.password == 'pass'
    assert api_with_auth.token is None
    assert api_with_auth.validate_certs is True

def test_initialization_with_cache_clear(api_with_cache_clear):
    assert api_with_cache_clear.galaxy == 'exampleGalaxy'
    assert api_with_cache_clear.name == 'exampleClient'
    assert api_with_cache_clear.api_server == 'https://api.ansiblegalaxy.com'
    assert api_with_cache_clear.username is None
    assert api_with_cache_clear.password is None
    assert api_with_cache_clear.token is None
    assert api_with_cache_clear.validate_certs is True
    assert not os.path.exists(api_with_cache_clear._b_cache_path)

def test_initialization_without_cache(api_without_cache):
    assert api_without_cache.galaxy == 'exampleGalaxy'
    assert api_without_cache.name == 'exampleClient'
    assert api_without_cache.api_server == 'https://api.ansiblegalaxy.com'
    assert api_without_cache.username is None
    assert api_without_cache.password is None
    assert api_without_cache.token is None
    assert api_without_cache.validate_certs is True
    assert not os.path.exists(api_without_cache._b_cache_path)

def test_initialization_with_priority(api_with_priority):
    assert api_with_priority.galaxy == 'exampleGalaxy'
    assert api_with_priority.name == 'exampleClient'
    assert api_with_priority.api_server == 'https://api.ansiblegalaxy.com'
    assert api_with_priority.username is None
    assert api_with_priority.password is None
    assert api_with_priority.token is None
    assert api_with_priority.validate_certs is True
    assert api_with_priority._priority == 1.0

def test_initialization_with_token(api_with_token):
    assert api_with_token.galaxy == 'exampleGalaxy'
    assert api_with_token.name == 'exampleClient'
    assert api_with_token.api_server == 'https://api.ansiblegalaxy.com'
    assert api_with_token.username is None
    assert api_with_token.password is None
    assert api_with_token.token == 'your_api_token'
    assert api_with_token.validate_certs is True
    assert api_with_token._priority == float('inf')

def test_initialization_with_all_params(api_with_all_params):
    assert api_with_all_params.galaxy == 'exampleGalaxy'
    assert api_with_all_params.name == 'exampleClient'
    assert api_with_all_params.api_server == 'https://api.ansiblegalaxy.com'
    assert api_with_all_params.username == 'user'
    assert api_with_all_params.password == 'pass'
    assert api_with_all_params.token is None
    assert api_with_all_params.validate_certs is True