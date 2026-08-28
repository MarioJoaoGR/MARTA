
import pytest
from ansible.module_utils.common.dict_transformations import camel_to_snake

def value_is_list(camel_list):
    """
    Recursively processes a list to convert dictionary keys from camelCase to snake_case and handles nested lists.
    
    Parameters:
        camel_list (list): A list containing dictionaries with camelCase keys, other lists, or other types.
        
    Returns:
        list: A new list where the dictionary keys are converted from camelCase to snake_case, and nested lists are processed recursively.
    """
    checked_list = []
    for item in camel_list:
        if isinstance(item, dict):
            checked_dict = {}
            for key, value in item.items():
                new_key = camel_to_snake(key)
                if isinstance(value, list):
                    checked_dict[new_key] = value_is_list(value)
                else:
                    checked_dict[new_key] = value
            checked_list.append(checked_dict)
        elif isinstance(item, list):
            checked_list.append(value_is_list(item))
        else:
            checked_list.append(item)
    return checked_list

# Test cases
def test_valid_case():
    example_input = [{'camelCaseKey': 123, 'anotherKey': [456, {'moreCamelCase': 789}]}]
    result = value_is_list(example_input)
    assert result == [{'snake_case_key': 123, 'another_key': [456, {'more_camel_case': 789}]}]

def test_edge_case():
    with pytest.raises(TypeError):
        value_is_list(None)

def test_invalid_input():
    with pytest.raises(TypeError):
        value_is_list('string')
