
import pytest
from ansible.galaxy.api import GalaxyAPI
import os
import tarfile
from ansible.errors import AnsibleError

# Test initialization with default settings
def test_GalaxyAPI_default():
    api_client = GalaxyAPI(galaxy='exampleGalaxy', name='exampleClient', url='https://api.ansiblegalaxy.com')
    assert api_client.galaxy == 'exampleGalaxy'
    assert api_client.name == 'exampleClient'
    assert api_client.api_server == 'https://api.ansiblegalaxy.com'