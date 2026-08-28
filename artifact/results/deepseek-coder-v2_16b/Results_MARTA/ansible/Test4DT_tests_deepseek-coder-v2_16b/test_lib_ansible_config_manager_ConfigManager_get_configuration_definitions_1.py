
import pytest
from ansible.config.manager import ConfigManager
import os


def test_invalid_conf_file():
    with pytest.raises(Exception):
        ConfigManager(conf_file='nonexistent/path/to/config.ini', defs_file='path/to/definitions.yml')

def test_missing_defs_file():
    with pytest.raises(Exception):
        ConfigManager(conf_file='path/to/config.ini', defs_file='nonexistent/path/to/definitions.yml')