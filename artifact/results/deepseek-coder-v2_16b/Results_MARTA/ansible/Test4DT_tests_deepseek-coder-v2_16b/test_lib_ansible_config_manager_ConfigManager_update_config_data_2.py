
import pytest
from ansible.config.manager import ConfigManager
import os


def test_edge_cases():
    edge_case_config = ConfigManager()  # No files provided, should default to base.yml if present
    assert isinstance(edge_case_config, ConfigManager)
    assert edge_case_config._config_file is None
    assert edge_case_config._base_defs != {}