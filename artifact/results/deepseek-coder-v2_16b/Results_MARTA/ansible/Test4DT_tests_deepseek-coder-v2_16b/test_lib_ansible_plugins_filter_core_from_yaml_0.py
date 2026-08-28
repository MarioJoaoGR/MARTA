
import pytest
from ansible.plugins.filter import core
import yaml

# Test valid YAML string input
def test_valid_yaml_string():
    data = 'key: value'
    result = core.from_yaml(data)
    assert isinstance(result, dict)
    assert result == {'key': 'value'}

# Test invalid input type
def test_invalid_input():
    data = 123
    result = core.from_yaml(data)
    assert result == 123

# Test handling of None input
def test_none_input():
    data = None
    result = core.from_yaml(data)
    assert result is None
