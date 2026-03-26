
import pytest
import tomllib
import configparser
import os
from typing import Any
from isort.settings import _get_config_data

@pytest.fixture(scope="module")
def valid_toml_file():
    with open("temp_test_toml.toml", "w") as f:
        f.write("[section1]\nkey1 = 'value1'\n[section2]\nkey2 = 'value2'")
    yield "temp_test_toml.toml"
    os.remove("temp_test_toml.toml")

@pytest.fixture(scope="module")
def valid_editorconfig_file():
    with open("temp_test_editorconfig", "w") as f:
        f.write("[section3]\nkey1 = 'value1'\n")
    yield "temp_test_editorconfig"
    os.remove("temp_test_editorconfig")

def test_get_config_data_toml(valid_toml_file):
    config_data = _get_config_data(valid_toml_file, ("section1", "section2"))
    assert isinstance(config_data, dict)
    assert "source" in config_data
    assert config_data["source"] == valid_toml_file

def test_get_config_data_editorconfig(valid_editorconfig_file):
    config_data = _get_config_data(valid_editorconfig_file, ("section3",))
    assert isinstance(config_data, dict)
    assert "source" in config_data
    assert config_data["source"] == valid_editorconfig_file

def test_get_config_data_toml_with_sections():
    with open("temp_test_toml.toml", "w") as f:
        f.write("[section1]\nkey1 = 'value1'\n[section2]\nkey2 = 'value2'")
    config_data = _get_config_data("temp_test_toml.toml", ("section1",))
    assert "source" in config_data