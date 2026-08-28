
import configparser
import pytest
from ansible.config.manager import get_ini_config_value

@pytest.fixture
def sample_config():
    # Create a ConfigParser instance and add some example data
    config = configparser.ConfigParser()
    config['user'] = {'name': 'John Doe', 'age': '30'}
    return config

# Test case to check if the function correctly retrieves the value when the key exists in the specified section
def test_get_ini_config_value_with_existing_key(sample_config):
    entry = {'section': 'user', 'key': 'name'}
    assert get_ini_config_value(sample_config, entry) == 'John Doe'

# Test case to verify that the function returns `None` when the key does not exist in the configuration object
def test_get_ini_config_value_with_missing_key(sample_config):
    entry = {'section': 'user', 'key': 'email'}
    assert get_ini_config_value(sample_config, entry) is None

# Test case to check the behavior with default values, ensuring that no section or key defined results in the expected outcome (`None`)
def test_get_ini_config_value_with_default_values():
    config = configparser.ConfigParser()
    entry_with_defaults = {'section': 'user', 'key': 'name'}  # Assuming 'name' exists in a default section