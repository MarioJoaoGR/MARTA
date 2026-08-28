
import pytest
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError, AnsibleOptionsError
import os

def test_invalid_configuration_file():
    with pytest.raises(AnsibleError) as excinfo:
        ConfigManager(conf_file='invalid_path', defs_file='invalid_path')
    assert "Missing base YAML definition file (bad install?): invalid_path" in str(excinfo.value)

