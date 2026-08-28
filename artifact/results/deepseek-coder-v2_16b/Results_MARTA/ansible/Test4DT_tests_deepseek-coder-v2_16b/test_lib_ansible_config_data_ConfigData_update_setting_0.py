
import pytest
from ansible.config.data import ConfigData, ConfigSetting, Plugin

# Test 1: Updating a global setting with valid input
def test_valid_input_global_setting():
    config = ConfigData()
    setting = ConfigSetting(name='log_level', value='DEBUG')
    config.update_setting(setting)
    assert config._global_settings['log_level'] == 'DEBUG'

# Test 2: Updating a plugin-specific setting with valid input
def test_valid_input_plugin_setting():
    config = ConfigData()
    plugin = Plugin(type='logging', name='file_logger')
    setting = ConfigSetting(name='log_level', value='INFO')
    config.update_setting(setting, plugin)
    assert config._plugins['logging']['file_logger']['log_level'] == 'INFO'

# Test 3: Updating a setting with None input, expecting TypeError
def test_invalid_input_none():
    config = ConfigData()
    setting = None
    with pytest.raises(TypeError):
        config.update_setting(setting)
