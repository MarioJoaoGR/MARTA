# Module: ansible.config.manager
import pytest
from ansible.config.manager import ConfigManager

# Test initialization with default files
def test_init_with_default_files():
    config_manager = ConfigManager()
    assert hasattr(config_manager, '_config_file')
    assert config_manager._config_file is not None
    assert hasattr(config_manager, 'data')
    assert isinstance(config_manager.data, ConfigData)

# Test initialization with custom configuration and definition files
def test_init_with_custom_files():
    config_manager = ConfigManager(conf_file='path/to/custom_config.ini', defs_file='path/to/custom_definitions.yml')
    assert hasattr(config_manager, '_config_file')
    assert config_manager._config_file == 'path/to/custom_config.ini'
    assert hasattr(config_manager, 'data')
    assert isinstance(config_manager.data, ConfigData)

# Test updating configuration data with default base definitions and config file
def test_update_config_data_default():
    config_manager = ConfigManager()
    config_manager.update_config_data()
    assert hasattr(config_manager.data, 'CONFIG_FILE')
    assert config_manager.data.CONFIG_FILE is not None

# Test updating configuration data with custom base definitions and config file
def test_update_config_data_custom():
    defs = {'custom': 'definition'}
    config_file = 'path/to/custom_config.ini'
    config_manager = ConfigManager()
    config_manager.update_config_data(defs=defs, configfile=config_file)
    assert hasattr(config_manager.data, 'CONFIG_FILE')
    assert config_manager.data.CONFIG_FILE == config_file

# Test updating configuration data with invalid definition type
def test_update_config_data_invalid_definition():
    defs = "invalid"
    with pytest.raises(AnsibleOptionsError):
        config_manager = ConfigManager()
        config_manager.update_config_data(defs=defs)

# Test updating configuration data with invalid config file path
def test_update_config_data_invalid_configfile():
    defs = {}
    config_file = None
    with pytest.raises(AnsibleOptionsError):
        config_manager = ConfigManager()
        config_manager.update_config_data(defs=defs, configfile=config_file)
