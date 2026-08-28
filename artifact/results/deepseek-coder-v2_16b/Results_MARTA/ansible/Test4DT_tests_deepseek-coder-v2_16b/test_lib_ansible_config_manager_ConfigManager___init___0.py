
import pytest
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError
import os



def test_invalid_inputs():
    non_existent_path = 'non/existent/path'
    with pytest.raises(AnsibleError):
        ConfigManager(conf_file=non_existent_path, defs_file=non_existent_path)