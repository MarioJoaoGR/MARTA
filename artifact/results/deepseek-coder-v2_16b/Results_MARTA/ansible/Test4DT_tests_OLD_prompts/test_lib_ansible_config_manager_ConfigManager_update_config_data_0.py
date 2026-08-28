
import pytest
from unittest.mock import patch
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleOptionsError, AnsibleError
import os
import sys
import traceback

@pytest.fixture
def config_manager():
    return ConfigManager()

@patch('ansible.config.manager.ConfigManager._read_config_yaml_file', return_value={})
def test_valid_inputs(mock_read_config):
    with pytest.raises(AnsibleOptionsError) as excinfo:
        config = ConfigManager(conf_file='path/to/config.yml', defs_file='path/to/definitions.yml')
    assert str(excinfo.value) == "Unsupported configuration file type: yaml"
