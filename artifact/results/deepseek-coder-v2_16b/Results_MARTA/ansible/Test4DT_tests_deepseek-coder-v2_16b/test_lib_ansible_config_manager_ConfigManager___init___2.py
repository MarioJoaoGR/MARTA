
import pytest
from ansible.config.manager import ConfigManager
import os


def test_edge_cases():
    cm = ConfigManager(conf_file=None, defs_file=None)
    assert cm._config_file is None
