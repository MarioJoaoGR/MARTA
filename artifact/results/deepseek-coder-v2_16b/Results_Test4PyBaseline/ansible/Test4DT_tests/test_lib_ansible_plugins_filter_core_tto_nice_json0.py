
import pytest
from ansible.plugins.filter import core
import json

# Test cases for the to_nice_json function
def test_to_nice_json_basic():
    result = core.to_nice_json({'key': 'value'})
    assert isinstance(result, str), "Expected a JSON string"
    parsed_result = json.loads(result)
    assert parsed_result == {'key': 'value'}, f"Unexpected output: {result}"

def test_to_nice_json_custom_indent():
    result = core.to_nice_json({'key': 'value'}, indent=2)
    assert isinstance(result, str), "Expected a JSON string"
    parsed_result = json.loads(result)
    assert parsed_result == {'key': 'value'}, f"Unexpected output: {result}"
    assert result == json.dumps({'key': 'value'}, indent=2), "Custom indentation did not match expected output"

def test_to_nice_json_sort_keys():
    result = core.to_nice_json({'b': 'value', 'a': 'another value'}, sort_keys=True)
    assert isinstance(result, str), "Expected a JSON string"
    parsed_result = json.loads(result)
    assert parsed_result == {'a': 'another value', 'b': 'value'}, f"Unexpected output: {result}"