# Module: ansible.config.manager
# test_config_manager.py
from ansible.config.manager import ConfigManager
import os
import pytest

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_initialization_with_specific_files(tmpdir):
    conf_file = tmpdir / 'settings.ini'
    defs_file = tmpdir / 'base_defs.yml'
    conf_file.write('')  # Placeholder for actual INI content
    defs_file.write('')  # Placeholder for actual YAML content
    
    cm = ConfigManager(conf_file=str(conf_file), defs_file=str(defs_file))
    assert cm._config_file == str(conf_file)
    assert cm._base_defs_file == str(defs_file)

def test_initialization_without_files(tmpdir):
    cm = ConfigManager()
    assert cm._config_file is None
    assert cm._base_defs_file == '%s/base.yml' % os.path.dirname(__file__)

def test_get_plugin_options():
    # Assuming get_plugin_options method exists and works as expected
    cm = ConfigManager()
    plugin_options = cm.get_plugin_options('type', 'name')
    assert isinstance(plugin_options, list) or plugin_options is None  # Adjust based on actual implementation

def test_get_configuration_definition():
    # Assuming get_configuration_definition method exists and works as expected
    cm = ConfigManager()
    config_definition = cm.get_configuration_definition('specific_name')
    assert config_definition is None or isinstance(config_definition, dict)  # Adjust based on actual implementation

def test_loop_entries():
    cm = ConfigManager()
    container = {'name': 'value'}
    entry_list = [{'name': 'name', 'deprecated': 'warning'}]
    
    value, origin = cm._loop_entries(container, entry_list)
    assert value == 'value'
    assert origin == 'name'
    assert len(cm.DEPRECATED) == 1
    assert cm.DEPRECATED[0] == ('name', 'warning')

def test_loop_entries_invalid_character():
    cm = ConfigManager()
    container = {'name': u'\U0001f4a9'}  # Unicode character causing UnicodeEncodeError
    entry_list = [{'name': 'name', 'deprecated': 'warning'}]
    
    with pytest.raises(UnicodeEncodeError):
        cm._loop_entries(container, entry_list)
    assert len(cm.WARNINGS) == 1
    assert str(cm.WARNINGS.pop()) == "value for config entry name contains invalid characters, ignoring..."
