
import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict

def test_valid_input():
    valid_input = {'first_name': 'John', 'last_name': 'Doe'}
    expected_output = {'firstName': 'John', 'lastName': 'Doe'}
    assert snake_dict_to_camel_dict(valid_input) == expected_output

def test_capitalize_first():
    valid_input = {'first_name': 'John', 'last_name': 'Doe'}
    expected_output = {'FirstName': 'John', 'LastName': 'Doe'}
    assert snake_dict_to_camel_dict(valid_input, capitalize_first=True) == expected_output
