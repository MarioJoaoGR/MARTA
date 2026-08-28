
import pytest
from ansible.plugins.filter import core
from yaml import safe_load_all
from six import string_types

# Test cases for from_yaml_all function
def test_from_yaml_all_string():
    """Test the function with a YAML-formatted string."""
    data = "key: value"
    result = core.from_yaml_all(data)
    expected_result = [{'key': 'value'}]
    assert list(result) == expected_result, f"Expected {expected_result}, but got {list(result)}"

def test_from_yaml_all_dict():
    """Test the function with a dictionary."""
    data = {"non": "YAML"}
    result = core.from_yaml_all(data)
    assert result == data, f"Expected {data}, but got {result}"

def test_from_yaml_all_list():
    """Test the function with a list of YAML-formatted strings."""
    yaml_list = [
        "key1: value1",
        "key2: value2"
    ]
    result = core.from_yaml_all(yaml_list)
    expected_result = [{'key1': 'value1'}, {'key2': 'value2'}]