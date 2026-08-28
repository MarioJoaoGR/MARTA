
# Module: ansible.config.manager
import os
from ansible.config.manager import get_config_type
from ansible.errors import AnsibleOptionsError
import pytest

def test_get_config_type_none():
    assert get_config_type(None) is None

def test_get_config_type_empty_string():
    with pytest.raises(AnsibleOptionsError):
        get_config_type('')

def test_get_config_type_ini():
    assert get_config_type('settings.ini') == 'ini'

def test_get_config_type_cfg():
    assert get_config_type('config.cfg') == 'ini'

def test_get_config_type_yaml():
    assert get_config_type('config.yaml') == 'yaml'

def test_get_config_type_yml():
    assert get_config_type('settings.yml') == 'yaml'

def test_get_config_type_unsupported():
    with pytest.raises(AnsibleOptionsError) as excinfo:
        get_config_type('data.txt')
    assert str(excinfo.value) == "Unsupported configuration file extension for data.txt: .txt"
