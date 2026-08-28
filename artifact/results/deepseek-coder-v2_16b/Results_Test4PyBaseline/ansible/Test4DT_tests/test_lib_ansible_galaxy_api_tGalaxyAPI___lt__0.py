
import pytest
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture(scope="module")
def default_api():
    return GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')

@pytest.fixture(scope="module")
def custom_auth_api():
    return GalaxyAPI(
        galaxy='exampleGalaxy', 
        name='exampleClient', 
        url='https://api.ansiblegalaxy.com', 
        username='user', 
        password='pass', 
        clear_response_cache=True, 
        no_cache=False
    )

@pytest.fixture(scope="module")
def token_auth_api():
    return GalaxyAPI(
        galaxy='exampleGalaxy', 
        name='exampleClient', 
        url='https://api.ansiblegalaxy.com', 
        token='your_api_token'
    )

@pytest.fixture(scope="module")
def no_tls_validation_api():
    return GalaxyAPI(
        galaxy='exampleGalaxy', 
        name='exampleClient', 
        url='https://api.ansiblegalaxy.com', 
        validate_certs=False
    )

@pytest.fixture(scope="module")
def specific_api_versions():
    return GalaxyAPI(
        galaxy='exampleGalaxy', 
        name='exampleClient', 
        url='https://api.ansiblegalaxy.com', 
        available_api_versions={'v1': 'http://api.ansiblegalaxy.com/v1'}
    )

@pytest.fixture(scope="module")
def custom_priority_api():
    return GalaxyAPI(
        galaxy='exampleGalaxy', 
        name='exampleClient', 
        url='https://api.ansiblegalaxy.com', 
        priority=10
    )

# Test cases for default initialization
def test_default_initialization(default_api):
    assert default_api.galaxy == 'exampleGalaxy'
    assert default_api.name == 'exampleClient'
    assert default_api.api_server == 'https://api.ansiblegalaxy.com'
    assert default_api.validate_certs is True
    assert not hasattr(default_api, 'username')
    assert not hasattr(default_api, 'password')
    assert default_api._priority == float('inf')

# Test cases for initialization with custom authentication and cache settings
def test_custom_auth_initialization(custom_auth_api):
    assert custom_auth_api.galaxy == 'exampleGalaxy'
    assert custom_auth_api.name == 'exampleClient'
    assert custom_auth_api.api_server == 'https://api.ansiblegalaxy.com'
    assert not hasattr(custom_auth_api, 'token')
    assert custom_auth_api.validate_certs is True
    assert custom_auth_api.username == 'user'
    assert custom_auth_api.password == 'pass'
    assert custom_auth_api.clear_response_cache is True
    assert custom_auth_api.no_cache is False
    assert custom_auth_api._priority == float('inf')

# Test cases for initialization with token authentication
def test_token_auth_initialization(token_auth_api):
    assert token_auth_api.galaxy == 'exampleGalaxy'
    assert token_auth_api.name == 'exampleClient'
    assert token_auth_api.api_server == 'https://api.ansiblegalaxy.com'
    assert token_auth_api.validate_certs is True
    assert not hasattr(token_auth_api, 'username')
    assert not hasattr(token_auth_api, 'password')
    assert token_auth_api.token == 'your_api_token'
    assert custom_auth_api._priority == float('inf')

# Test cases for initialization with TLS certificate validation disabled
def test_no_tls_validation_initialization(no_tls_validation_api):
    assert no_tls_validation_api.galaxy == 'exampleGalaxy'
    assert no_tls_validation_api.name == 'exampleClient'
    assert no_tls_validation_api.api_server == 'https://api.ansiblegalaxy.com'
    assert no_tls_validation_api.validate_certs is False
    assert not hasattr(no_tls_validation_api, 'username')
    assert not hasattr(no_tls_validation_api, 'password')
    assert custom_auth_api._priority == float('inf')

# Test cases for initialization with specific API versions
def test_specific_api_versions_initialization(specific_api_versions):
    assert specific_api_versions.galaxy == 'exampleGalaxy'
    assert specific_api_versions.name == 'exampleClient'
    assert specific_api_versions.api_server == 'https://api.ansiblegalaxy.com'
    assert specific_api_versions.validate_certs is True
    assert not hasattr(specific_api_versions, 'username')
    assert not hasattr(specific_api_versions, 'password')
    assert specific_api_versions._available_api_versions == {'v1': 'http://api.ansiblegalaxy.com/v1'}
    assert custom_auth_api._priority == float('inf')

# Test cases for initialization with custom priority
def test_custom_priority_initialization(custom_priority_api):
    assert custom_priority_api.galaxy == 'exampleGalaxy'
    assert custom_priority_api.name == 'exampleClient'
    assert custom_priority_api.api_server == 'https://api.ansiblegalaxy.com'
    assert custom_priority_api.validate_certs is True
    assert not hasattr(custom_priority_api, 'username')
    assert not hasattr(custom_priority_api, 'password')
    assert custom_priority_api._priority == 10
    assert custom_auth_api._priority == float('inf')
