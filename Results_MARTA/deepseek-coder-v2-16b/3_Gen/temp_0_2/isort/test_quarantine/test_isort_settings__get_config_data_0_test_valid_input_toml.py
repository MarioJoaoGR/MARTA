
import pytest
from isort.settings import _get_config_data
import tomllib
import configparser
import os

@pytest.fixture(scope="module")
def valid_toml_file():
    # Create a temporary TOML file for testing
    data = {"section1": {"key1": "value1", "key2": "value2"}, "section2": {"key3": "value3"}}
    with open("test.toml", "wb") as f:
        tomllib.dump(data, f)
    yield "test.toml"
    os.remove("test.toml")

@pytest.fixture(scope="module")
def valid_ini_file():
    # Create a temporary INI file for testing
    with open("test.ini", "w") as f:
        f.write("[section3]\noption1 = value3\n")
    yield "test.ini"
    os.remove("test.ini")

def test_valid_input_toml(valid_toml_file):
    config_data = _get_config_data(valid_toml_file, ("section1", "section2"))
    assert config_data == {"key1": "value1", "key2": "value2", "source": valid_toml_file}

def test_valid_input_ini(valid_ini_file):
    config_data = _get_config_data(valid_ini_file, ("section3",))
    assert config_data == {"option1": "value3", "source": valid_ini_file}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__get_config_data_0_test_valid_input_toml
isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_input_toml.py:13:8: E1101: Module 'tomllib' has no 'dump' member (no-member)


"""