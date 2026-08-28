
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.filter.core import from_yaml_all

# Test for valid YAML string input
def test_valid_input_string():
    yaml_data = "key: value"
    with patch('ansible.plugins.filter.core.yaml_load_all', return_value=[{'key': 'value'}]):
        result = from_yaml_all(yaml_data)
        assert isinstance(result, list), "Result should be a list"
        assert len(result) == 1 and result[0] == {'key': 'value'}, "Result should contain the parsed object"

# Test for valid Python object input
def test_valid_input_object():
    loaded_object = {"another_key": "another_value"}
    with patch('ansible.plugins.filter.core.yaml_load_all', return_value=loaded_object):
        result = from_yaml_all(loaded_object)
        assert result == loaded_object, "Result should be the same as input"

# Test for handling of None input
def test_invalid_input_none():
    data = None
    with patch('ansible.plugins.filter.core.yaml_load_all', return_value=data):
        result = from_yaml_all(data)
        assert result is None, "Result should be None"
