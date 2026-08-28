
import pytest
from ansible.galaxy.api import GalaxyAPI

# Test 1: Initialize GalaxyAPI with default settings
def test_initialize_with_default_settings():
    api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
    assert api_client.galaxy == 'default_galaxy'
    assert api_client.name == 'default_name'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True
    assert api_client._priority == float('inf')

# Test 2: Initialize GalaxyAPI with authentication details and disable TLS certificate validation

# Test 3: Clear response cache if requested