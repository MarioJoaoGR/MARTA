# Module: ansible.config.manager
import pytest
from your_module import ConfigManager, ConfigData, Setting, Plugin

# Test initialization with configuration and definitions files
def test_init_with_files():
    cm = ConfigManager(conf_file='settings.ini', defs_file='base_defs.yml')
    assert isinstance(cm, ConfigManager)
    assert cm._config_file is not None
    assert cm._base_defs is not None

# Test initialization without files
def test_init_without_files():
    cm = ConfigManager()
    assert isinstance(cm, ConfigManager)
    assert cm._config_file is not None
    assert cm._base_defs is not None

# Test retrieving plugin options
def test_get_plugin_options():
    cm = ConfigManager(conf_file='settings.ini', defs_file='base_defs.yml')
    plugin_options = cm.get_plugin_options('type', 'name')
    assert isinstance(plugin_options, dict)

# Test retrieving configuration definition
def test_get_configuration_definition():
    cm = ConfigManager(conf_file='settings.ini', defs_file='base_defs.yml')
    config_definition = cm.get_configuration_definition('name', plugin_type='type', plugin_name='name')
    assert isinstance(config_definition, dict) or config_definition is None

# Test updating configuration settings
def test_update_setting():
    cm = ConfigManager(conf_file='settings.ini', defs_file='base_defs.yml')
    setting_to_update = Setting('new_log_level', 'INFO')
    cm.update_setting(setting_to_update)
    assert cm.data._global_settings['new_log_level'] == 'INFO'

# Test initializing ConfigData and updating settings
def test_config_data_initialization():
    config_data = ConfigData()
    global_setting = Setting('log_level', 'DEBUG')
    config_data.update_setting(global_setting)
    assert config_data._global_settings['log_level'] == 'DEBUG'
    
    plugin = Plugin('logging', 'logger1')
    plugin_setting = Setting('format', 'json')
    config_data.update_setting(plugin_setting, plugin)
    assert config_data._plugins['logging']['logger1']['format'] == 'json'
