
import configparser
import pytest
from ansible.config.manager import get_ini_config_value

@pytest.fixture
def sample_config():
    # Create a ConfigParser instance and add some example data
    config = configparser.ConfigParser()
    config['user'] = {'name': 'John Doe', 'age': '30'}
    return config

def test_get_ini_config_value_with_existing_key(sample_config):
    entry = {'section': 'user', 'key': 'name'}
    assert get_ini_config_value(sample_config, entry) == 'John Doe'

def test_get_ini_config_value_with_missing_key(sample_config):
    entry = {'section': 'user', 'key': 'email'}
    assert get_ini_config_value(sample_config, entry) is None

def test_get_ini_config_value_with_default_values():
    config = configparser.ConfigParser()
    entry_with_defaults = {'section': 'user', 'key': 'name'}  # Assuming 'name' exists in a default section
    assert get_ini_config_value(config, entry_with_defaults) is None

def test_get_ini_config_value_with_missing_section():
    config = configparser.ConfigParser()
    config['non_existent_section'] = {'name': 'Jane Doe'}  # Adding a default section for demonstration
    entry_with_missing_section = {'section': 'non_existent_section', 'key': 'name'}
    assert get_ini_config_value(config, entry_with_missing_section) == 'Jane Doe'

def test_get_ini_config_value_with_none_input():
    with pytest.raises(TypeError):  # Ensure the function raises a TypeError if None is passed as input
        get_ini_config_value(None, {'section': 'user', 'key': 'name'})
