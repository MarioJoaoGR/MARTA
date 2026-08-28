# Module: ansible.config.data
import pytest
from ansible.config.data import ConfigData

# Test initialization of ConfigData instance
def test_init():
    config = ConfigData()
    assert isinstance(config._global_settings, dict)
    assert config._global_settings == {}
    assert isinstance(config._plugins, dict)
    assert config._plugins == {}

# Test getting global settings without a plugin
def test_get_settings_no_plugin():
    config = ConfigData()
    # Assuming update_setting is not implemented yet, we will manually set the setting for testing
    config._global_settings['log_level'] = 'DEBUG'
    settings = config.get_settings()
    assert isinstance(settings, list)
    assert len(settings) == 1
    assert settings[0] == 'DEBUG'

# Test getting settings for a specific plugin
def test_get_settings_with_plugin():
    config = ConfigData()
    # Assuming update_setting is not implemented yet, we will manually set the setting for testing
    config._plugins['logging'] = {}
    config._plugins['logging']['logger1'] = {'format': 'json'}
    plugin = type('Plugin', (object,), {'type': 'logging', 'name': 'logger1'})()
    settings = config.get_settings(plugin)
    assert isinstance(settings, list)
    assert len(settings) == 1
    assert settings[0] == 'json'

# Test getting a specific global setting
def test_get_setting():
    config = ConfigData()
    # Assuming update_setting is not implemented yet, we will manually set the setting for testing
    config._global_settings['log_level'] = 'DEBUG'
    setting = config.get_setting('log_level')
    assert isinstance(setting, str)
    assert setting == 'DEBUG'

# Test getting a specific plugin-specific setting
def test_get_setting_with_plugin():
    config = ConfigData()
    # Assuming update_setting is not implemented yet, we will manually set the setting for testing
    config._plugins['logging'] = {}
    config._plugins['logging']['logger1'] = {'format': 'json'}
    plugin = type('Plugin', (object,), {'type': 'logging', 'name': 'logger1'})()
    setting = config.get_setting('format', plugin)
    assert isinstance(setting, str)
    assert setting == 'json'
