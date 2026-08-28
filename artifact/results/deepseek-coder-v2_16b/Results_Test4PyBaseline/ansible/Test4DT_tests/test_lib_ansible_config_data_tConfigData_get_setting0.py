# Module: ansible.config.data
import pytest
from ansible.config.data import ConfigData

# Fixture to create a ConfigData instance for each test
@pytest.fixture
def config():
    return ConfigData()

# Test case for retrieving a global setting
def test_get_global_setting(config):
    # Arrange: No specific plugin, just the global settings
    # Act: Retrieve a non-existent global setting
    result = config.get_setting('non_existent_setting')
    # Assert: The result should be None as the setting does not exist
    assert result is None

# Test case for retrieving a plugin-specific setting
def test_get_plugin_setting(config):
    # Arrange: Define a mock plugin with type and name
    class MockPlugin:
        def __init__(self, typ, nam):
            self.type = typ
            self.name = nam
    
    plugin = MockPlugin('logging', 'logger1')
    # Act: Retrieve a non-existent setting for the mock plugin
    result = config.get_setting('non_existent_setting', plugin)
    # Assert: The result should be None as the setting does not exist
    assert result is None

# Test case for retrieving an existing global setting
def test_get_existing_global_setting(config):
    # Arrange: Set a global setting
    config._global_settings['log_level'] = 'DEBUG'
    # Act: Retrieve the set global setting
    result = config.get_setting('log_level')
    # Assert: The result should be 'DEBUG' as it is the set value
    assert result == 'DEBUG'

# Test case for retrieving an existing plugin-specific setting
def test_get_existing_plugin_setting(config):
    # Arrange: Set a plugin-specific setting
    config._plugins['logging']['logger1'] = {'format': 'JSON'}
    # Define a mock plugin with type and name
    class MockPlugin:
        def __init__(self, typ, nam):
            self.type = typ
            self.name = nam
    
    plugin = MockPlugin('logging', 'logger1')
    # Act: Retrieve the set plugin-specific setting
    result = config.get_setting('format', plugin)
    # Assert: The result should be 'JSON' as it is the set value
    assert result == 'JSON'
