
import pytest
from ansible.plugins.filter.core import to_nice_json
import json

# Test scenario 1: Valid input - happy path
def test_valid_input_happy_path():
    data = {'key': 'value'}
    result = to_nice_json(data)
    expected_output = json.dumps({'key': 'value'}, indent=4, sort_keys=True, separators=(',', ': '))
    assert result == expected_output

# Test scenario 2: Edge case - None input
def test_edge_case_none():
    data = None
    with pytest.raises(TypeError):
        to_nice_json(data)

# Test scenario 3: Invalid input - error handling
def test_invalid_input_error_handling():
    data = 'invalid'
    with pytest.raises(TypeError):
        to_nice_json(data)
