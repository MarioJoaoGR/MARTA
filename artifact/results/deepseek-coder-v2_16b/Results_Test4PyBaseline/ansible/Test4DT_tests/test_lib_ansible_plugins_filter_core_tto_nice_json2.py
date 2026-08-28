
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

# New test case to cover the uncovered line (73)
def test_to_nice_json_default_parameters():
    result = core.to_nice_json({'key': 'value'})
    assert isinstance(result, str), "Expected a JSON string"
    parsed_result = json.loads(result)
    expected_output = {'key': 'value'}
    # Check if the default parameters are correctly passed to the underlying to_json function
    assert parsed_result == expected_output, f"Unexpected output: {result}"
    # Additional check to ensure the separators are set as expected
    json_str = json.dumps(expected_output, indent=4, sort_keys=True, separators=(',', ': '))
    assert result == json_str, "Default parameters did not match expected output"
