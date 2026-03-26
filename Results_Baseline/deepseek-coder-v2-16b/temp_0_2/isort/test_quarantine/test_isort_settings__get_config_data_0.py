
import pytest
import tomllib
import configparser
import os
from typing import Any

# Assuming _get_config_data is defined in the module 'isort.settings'
from isort.settings import _get_config_data

@pytest.fixture(scope="module")
def sample_toml():
    return """
[server]
host = "localhost"
port = 8080

[database]
user = "admin"
password = "secret"
"""

@pytest.fixture(scope="module")
def sample_editorconfig():
    return """
# Editor configuration for settings
[editor]
indent_style = space
indent_size = 2
max_line_length = off
"""

def test_get_config_data_toml(sample_toml):
    # Test retrieving configuration data from a TOML file
    with open("config.toml", "w") as f:
        f.write(sample_toml)
    config_data = _get_config_data('config.toml', ('server', 'database'))
    assert isinstance(config_data, dict)
    assert "source" in config_data
    assert config_data["source"] == "config.toml"
    assert config_data["host"] == "localhost"