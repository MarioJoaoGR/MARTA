# Module: ansible.config.manager
# test_manager.py
from ansible.config.manager import _get_entry

def test_all_parameters_provided():
    result = _get_entry('type1', 'pluginA', 'conf1')
    assert result == 'plugin_type: type1 plugin: pluginA setting: conf1'

def test_only_config_parameter():
    result = _get_entry(None, None, 'conf2')
    assert result == 'setting: conf2'

def test_only_plugin_type_and_config():
    result = _get_entry('type2', None, 'conf3')
    assert result == 'plugin_type: type2 setting: conf3'

def test_only_config_parameter():
    result = _get_entry(None, None, 'conf4')
    assert result == 'setting: conf4'
