
import configparser
import pytest
from ansible.config.manager import get_ini_config_value

@pytest.fixture
def sample_config():
    # Create a ConfigParser instance and add some example data
    config = configparser.ConfigParser()
    config['user'] = {'name': 'John Doe', 'age': '30'}
    return config

# Test case for the default value when p is None
def test_get_ini_config_value_with_none_input():
    assert get_ini_config_value(None, {'section': 'user', 'key': 'name'}) is None

# Test case to ensure that the function returns the correct value for an existing key
def test_get_ini_config_value_with_existing_key(sample_config):
    entry = {'section': 'user', 'key': 'name'}
    assert get_ini_config_value(sample_config, entry) == 'John Doe'

# Test case to ensure that the function returns None for a missing key within an existing section
def test_get_ini_config_value_with_missing_key(sample_config):
    entry = {'section': 'user', 'key': 'email'}
    assert get_ini_config_value(sample_config, entry) is None

# Test case to ensure that the function returns None for a missing section and key
def test_get_ini_config_value_with_missing_section():
    config = configparser.ConfigParser()
    config['non_existent_section'] = {'name': 'Jane Doe'}  # Adding a default section for demonstration
    entry_with_missing_section = {'section': 'non_existent_section', 'key': 'name'}