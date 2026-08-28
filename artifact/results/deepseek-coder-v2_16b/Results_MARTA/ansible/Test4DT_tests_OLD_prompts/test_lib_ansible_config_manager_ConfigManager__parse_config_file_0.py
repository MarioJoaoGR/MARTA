
import pytest
from unittest.mock import patch, MagicMock
from ansible.config.manager import ConfigManager, find_ini_config_file
from ansible.errors import AnsibleError, AnsibleOptionsError
import os
import configparser



def test_missing_defs_file():
    with patch('ansible.config.manager.find_ini_config_file', return_value='path/to/valid/config.yml'):
        with pytest.raises(AnsibleError):
            ConfigManager(conf_file='path/to/valid/config.yml', defs_file=None)