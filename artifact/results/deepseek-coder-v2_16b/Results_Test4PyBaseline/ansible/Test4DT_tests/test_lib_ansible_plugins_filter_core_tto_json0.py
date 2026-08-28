# Module: ansible.plugins.filter.core
import pytest
import json
from ansible.utils.json_encoder import AnsibleJSONEncoder
from ansible.plugins.filter.core import to_json

# Test cases for the to_json function

def test_to_json_dict():
    data = {'key': 'value'}
    result = to_json(data)
    assert isinstance(result, str), "Expected a JSON string"
    expected_output = json.dumps({'key': 'value'})
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_to_json_int_pretty():
    data = 42
    result = to_json(data, indent=4)
    assert isinstance(result, str), "Expected a JSON string"
    expected_output = json.dumps(42, indent=4)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_to_json_custom_encoder():
    class CustomEncoder(AnsibleJSONEncoder):
        pass
    
    custom_encoder = CustomEncoder()
    data = {'key': 'value'}
    result = to_json(data, cls=custom_encoder)
    assert isinstance(result, str), "Expected a JSON string"
    expected_output = json.dumps({'key': 'value'}, cls=CustomEncoder)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_to_json_invalid_input():
    with pytest.raises(TypeError):
        to_json(None)  # None is not serializable by json.dumps without a custom encoder
