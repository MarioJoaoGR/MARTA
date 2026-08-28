# Module: ansible.config.manager
import os
from ansible.config.manager import get_config_type
from ansible.errors import AnsibleOptionsError

def test_get_config_type_ini():
    assert get_config_type('settings.ini') == 'ini'

def test_get_config_type_yaml():
    assert get_config_type('config.yaml') == 'yaml'

def test_get_config_type_unsupported():
    try:
        get_config_type('data.txt')
    except AnsibleOptionsError as e:
        assert str(e) == "Unsupported configuration file extension for data.txt: .txt"
