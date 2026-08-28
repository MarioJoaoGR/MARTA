
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

def test_get_config_type_no_extension():
    with pytest.raises(AnsibleOptionsError):
        get_config_type('nofile')

def test_get_config_type_ini_with_dot():
    assert get_config_type('settings.ini') == 'ini'

def test_get_config_type_yaml_with_dot():
    assert get_config_type('config.yaml') == 'yaml'

def test_get_config_type_unsupported_extension():
    with pytest.raises(AnsibleOptionsError):
        get_config_type('data.txt')
