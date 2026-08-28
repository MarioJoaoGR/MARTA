
import pytest
from ansible.plugins.filter.core import to_nice_json
import json

def test_valid_inputs():
    result = to_nice_json({'key': 'value'})
    assert isinstance(result, str), "Expected a string"
    try:
        parsed_result = json.loads(result)  # Attempt to parse the JSON string
        assert isinstance(parsed_result, dict), "Parsed result should be a dictionary"
    except ValueError as e:
        pytest.fail(f"Failed to parse JSON string: {e}")

def test_edge_cases():
    with pytest.raises(TypeError):
        # The function is expected to raise TypeError for unsupported input types
        to_nice_json()  # Call without arguments to trigger the TypeError
