
import pytest
import json
from your_module import jsonify  # Replace 'your_module' with the actual module name where jsonify is defined

# Test scenario 1: Test standard input with a dictionary
def test_valid_input_dict():
    result = {'key': 'value'}
    expected_output = json.dumps({'key': 'value'}, indent=4)
    assert jsonify(result) == expected_output

# Test scenario 2: Test formatting output
def test_format_output():
    result = [1, 2, 3]
    expected_output = json.dumps([1, 2, 3], indent=4)
    assert jsonify(result, format=True) == expected_output

# Test scenario 3: Test handling None input
def test_none_input():
    result = None
    expected_output = "{}"
    assert jsonify(result) == expected_output
