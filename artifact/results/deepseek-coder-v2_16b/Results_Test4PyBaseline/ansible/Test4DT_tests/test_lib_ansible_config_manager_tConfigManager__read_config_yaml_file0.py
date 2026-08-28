
# Module: ansible.config.manager
# test_config_manager.py
from ansible.config.manager import ConfigManager, AnsibleError
import pytest
import os
import yaml
from unittest.mock import patch, MagicMock

@pytest.fixture
def config_manager():
    return ConfigManager(conf_file='settings.ini', defs_file='base_defs.yml')

def test_config_manager_initialization_with_custom_files():
    cm = ConfigManager(conf_file='settings.ini', defs_file='base_defs.yml')
    assert cm._config_file == 'settings.ini'
    assert cm._base_defs is not None
    assert isinstance(cm._base_defs, dict)

def test_config_manager_initialization_without_files():
    with patch('ansible.config.manager.find_ini_config_file', return_value='found_ini'):
        cm = ConfigManager()
        assert cm._config_file == 'found_ini'
        assert cm.data is not None

def test_read_config_yaml_file_existing_file(tmp_path):
    yml_file = tmp_path / "base.yml"
    yml_file.write_text(yaml.dump({'key': 'value'}))
    cm = ConfigManager()
    result = cm._read_config_yaml_file(str(yml_file))
    assert result == {'key': 'value'}

def test_read_config_yaml_file_missing_file():
    with pytest.raises(AnsibleError):
        cm = ConfigManager()
        cm._read_config_yaml_file('nonexistent_file')

@patch('ansible.config.manager.self._parse_config_file', return_value=None)
def test_parse_config_file_mocked(mocker):
    cm = ConfigManager()
    assert cm._parse_config_file() is None
