
import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.token import GalaxyToken
import configparser
import os

@pytest.fixture
def galaxy_token():
    return GalaxyToken('initial_token')

def test_get_token(galaxy_token):
    assert galaxy_token.get() == 'initial_token'

def test_set_token(galaxy_token):
    galaxy_token.set('new_token')  # Corrected method name to match the class definition
    assert galaxy_token._token == 'new_token'
    with open(galaxy_token.b_file, 'r') as f:
        config = configparser.ConfigParser()
        config.read_string('[token]\nvalue=new_token')
    assert config['token']['value'] == 'new_token'

def test_save_token(galaxy_token):
    galaxy_token.set('new_token')  # Corrected method name to match the class definition
    with patch.object(os, 'makedirs'):
        galaxy_token.save()
    with open(galaxy_token.b_file, 'r') as f:
        config = configparser.ConfigParser()
        config.read_string('[token]\nvalue=new_token')