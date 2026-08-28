
import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

# Test Scenario 1: Valid input - happy path
def test_valid_input_happy_path():
    camel_dict = {'camelCaseKey': 'value', 'anotherCamelCaseKey': {'nestedKey': 'nestedValue'}}
    expected_output = {'camel_case_key': 'value', 'another_camel_case_key': {'nested_key': 'nestedValue'}}
    
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected_output

# Test Scenario 2: Edge case - handling None input
def test_edge_case_none():
    with pytest.raises(TypeError):
        camel_dict_to_snake_dict(None)

# Test Scenario 3: Invalid input - error handling for invalid input type
def test_invalid_input_error_handling():
    with pytest.raises(TypeError):
        camel_dict_to_snake_dict({'type': 'not a dictionary'})
