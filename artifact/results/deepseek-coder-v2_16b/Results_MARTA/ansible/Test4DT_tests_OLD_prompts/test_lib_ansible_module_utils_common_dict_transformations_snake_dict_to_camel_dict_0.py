
import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict

def test_valid_input():
    snake_dict = {'first_name': 'John', 'last_name': 'Doe'}
    camel_dict = snake_dict_to_camel_dict(snake_dict)
    assert camel_dict == {'firstName': 'John', 'lastName': 'Doe'}

def test_valid_input_capitalize_first():
    snake_dict = {'first_name': 'John', 'last_name': 'Doe'}
    camel_dict = snake_dict_to_camel_dict(snake_dict, capitalize_first=True)
    assert camel_dict == {'FirstName': 'John', 'LastName': 'Doe'}
