
import pytest
from your_module_name import ConfigData  # Replace 'your_module_name' with the actual module name where ConfigData is defined

@pytest.fixture
def config():
    return ConfigData()

# Test Scenario 1: Retrieving a global setting with valid input
def test_valid_input_global_setting(config):
    config.set_global_setting('log_level', 'INFO')
    assert config.get_global_setting('log_level') == 'INFO'

# Test Scenario 2: Retrieving a plugin-specific setting with valid input
def test_valid_input_plugin_setting(config):
    config.add_plugin('logging', {'file': 'logs/app.log', 'level': 'DEBUG'})
    config.set_global_setting('log_format', 'simple')
    assert config.get_plugin('logging') == {'file': 'logs/app.log', 'level': 'DEBUG'}
    assert config.get_global_setting('log_format') == 'simple'

# Test Scenario 3: Retrieving a setting with None input
def test_invalid_input_none(config):
    assert config.get_setting('unknown_key') is None
