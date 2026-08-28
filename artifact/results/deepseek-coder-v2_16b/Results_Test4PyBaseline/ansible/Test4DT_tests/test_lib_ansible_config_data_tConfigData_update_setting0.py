# Module: ansible.config.data
import pytest
from ansible.config.data import ConfigData
from ansible.config.models import Setting, Plugin

# Test initialization of ConfigData class
def test_init():
    config = ConfigData()
    assert isinstance(config._global_settings, dict)
    assert config._global_settings == {}
    assert isinstance(config._plugins, dict)
    assert config._plugins == {}

# Test updating a global setting
def test_update_setting_global():
    config = ConfigData()
    setting = Setting('log_level', 'DEBUG')
    config.update_setting(setting)
    assert config._global_settings['log_level'] == 'DEBUG'

# Test updating a plugin-specific setting
def test_update_setting_plugin():
    config = ConfigData()
    plugin = Plugin('logging', 'logger1')
    setting = Setting('format', 'json')
    config.update_setting(setting, plugin)
    assert config._plugins['logging']['logger1']['format'] == 'json'

# Test updating a global setting without specifying a plugin
def test_update_setting_global_no_plugin():
    config = ConfigData()
    setting = Setting('log_level', 'DEBUG')
    config.update_setting(setting)
    assert config._global_settings['log_level'] == 'DEBUG'

# Test updating a setting with an invalid plugin type (should not affect the global settings)
def test_update_setting_invalid_plugin():
    config = ConfigData()
    plugin = Plugin('invalid', 'logger1')
    setting = Setting('format', 'json')
    config.update_setting(setting, plugin)
    assert 'format' not in config._global_settings
    assert 'logging' not in config._plugins
