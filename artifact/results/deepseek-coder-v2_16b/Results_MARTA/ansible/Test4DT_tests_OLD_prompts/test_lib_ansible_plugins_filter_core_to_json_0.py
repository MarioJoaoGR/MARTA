
import pytest
from ansible.plugins.filter.core import to_json
import json
from unittest.mock import patch, MagicMock

# Test for valid input with default settings
def test_valid_input_default_settings():
    valid_input = {'key': 'value'}
    result = to_json(valid_input)
    assert isinstance(result, str), "Expected a JSON string"
    try:
        json.loads(result)
    except NameError:
        pytest.fail("NameError: name 'json' is not defined")

# Test for valid input with custom indentation
def test_valid_input_custom_indent():
    valid_input = {'key': 'value'}
    result = to_json(valid_input, indent=4)
    assert isinstance(result, str), "Expected a JSON string"
    try:
        json.loads(result)
    except NameError:
        pytest.fail("NameError: name 'json' is not defined")

# Test for invalid input (None)
def test_invalid_input_none():
    with patch('ansible.plugins.filter.core.to_json', return_value='null'):
        result = to_json(None)
        assert isinstance(result, str), "Expected a JSON string"
        try:
            json.loads(result)
        except NameError:
            pytest.fail("NameError: name 'json' is not defined")
