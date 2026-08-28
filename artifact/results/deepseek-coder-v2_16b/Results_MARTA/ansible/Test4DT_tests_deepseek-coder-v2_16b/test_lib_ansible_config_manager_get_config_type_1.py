
import pytest
from ansible.config.manager import get_config_type
from ansible.errors import AnsibleOptionsError
import os

# Test for valid INI file
def test_valid_ini_file():
    config_type = get_config_type('settings.ini')
    assert config_type == 'ini'

# Test for valid YAML file
def test_valid_yaml_file():
    config_type = get_config_type('database.yml')
    assert config_type == 'yaml'

# Test for invalid extension which should raise AnsibleOptionsError
def test_invalid_extension():
    with pytest.raises(AnsibleOptionsError) as excinfo:
        get_config_type('app.conf')
    assert str(excinfo.value) == "Unsupported configuration file extension for app.conf: .conf"
