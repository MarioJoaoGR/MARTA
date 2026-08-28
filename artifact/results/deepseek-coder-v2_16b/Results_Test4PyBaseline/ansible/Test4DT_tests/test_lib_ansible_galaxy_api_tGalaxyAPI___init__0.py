
# Module: ansible.galaxy.api
import pytest
from ansible.galaxy.api import GalaxyAPI
import os
import tempfile

# Test initialization with default settings
def test_default_initialization():
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')
    assert api_client.galaxy == 'exampleGalaxy'
    assert api_client.name == 'exampleClient'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'
    assert api_client.validate_certs is True