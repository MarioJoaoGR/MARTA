
import pytest
from ansible.config.manager import get_config_type, AnsibleOptionsError
import os

# Test for a valid INI file
def test_valid_ini_file():
    config_type = get_config_type('settings.ini')
    assert config_type == 'ini'

# Test for a valid YAML file
def test_valid_yaml_file():
    config_type = get_config_type('database.yml')
    assert config_type == 'yaml'

# Test for an invalid extension that should raise AnsibleOptionsError
def test_invalid_extension():
    with pytest.raises(AnsibleOptionsError) as excinfo:
        get_config_type('app.conf')
    assert str(excinfo.value) == "Unsupported configuration file extension for app.conf: .conf"
