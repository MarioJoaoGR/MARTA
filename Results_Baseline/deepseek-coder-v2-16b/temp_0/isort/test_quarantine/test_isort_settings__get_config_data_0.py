
import pytest
import tomllib
import configparser
import os
from typing import Any

# Assuming _get_config_data is defined in the module 'isort.settings'
from isort.settings import _get_config_data

@pytest.fixture(scope="module")
def valid_toml_file():
    # Create a temporary TOML file for testing
    with open("temp_test_toml.toml", "w") as f:
        f.write("[section1]\nkey1 = 'value1'\n[section2]\nkey2 = 'value2'")
    yield "temp_test_toml.toml"
    os.remove("temp_test_toml.toml")

@pytest.fixture(scope="module")
def valid_editorconfig_file():
    # Create a temporary editorconfig file for testing
    with open("temp_test_editorconfig", "w") as f:
        f.write("[section3]\nkey1 = 'value1'\n")
    yield "temp_test_editorconfig"
    os.remove("temp_test_editorconfig")

def test_get_config_data_toml(valid_toml_file):
    # Test retrieving configuration data from a TOML file
    config_data = _get_config_data(valid_toml_file, ("section1", "section2"))
    assert isinstance(config_data, dict)
    assert "source" in config_data
    assert config_data["source"] == valid_toml_file