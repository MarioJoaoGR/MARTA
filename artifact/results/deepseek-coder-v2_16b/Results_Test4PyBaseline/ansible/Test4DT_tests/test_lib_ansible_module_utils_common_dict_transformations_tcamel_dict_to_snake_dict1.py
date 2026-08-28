
import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

# Helper function to convert camelCase to snake_case for keys
def _camel_to_snake(name, reversible=False):
    if not reversible:
        # Convert camelCase to snake_case
        new_name = ''
        for i, char in enumerate(name):
            if char.isupper() and i != 0:
                new_name += '_' + char.lower()
            else:
                new_name += char.lower()
        return new_name
    else:
        # Handle reversible conversion by preserving pluralized abbreviations
        parts = []
        non_capitals = ''
        for i, char in enumerate(name):
            if char.isupper():
                if non_capitals:
                    parts.append(non_capitals)
                    non_capitals = ''
                parts.append(char.lower())
            else:
                non_capitals += char
        if non_capitals:
            parts.append(non_capitals)
        return '_'.join(parts)

# Test cases for camel_dict_to_snake_dict function
def test_camel_dict_to_snake_dict():
    # Basic usage
    camel_dict = {'camelCaseKey': 'value', 'anotherCamelCaseKey': {'nestedCamelCase': 'nestedValue'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {'camel_case_key': 'value', 'another_camel_case_key': {'nested_camel_case': 'nestedValue'}}

def test_camel_dict_to_snake_dict_reversible():
    # With reversible parameter set to True
    camel_dict = {'camelCaseKey': 'value', 'anotherCamelCaseKey': {'nestedCamelCase': 'nestedValue'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict, reversible=True)
    assert snake_dict == {'camel_case_key': 'value', 'another_camel_case_key': {'nested_camel_case': 'nestedValue'}}

def test_camel_dict_to_snake_dict_ignore_list():
    # With ignore_list parameter
    ignore_list = ('tags',)
    camel_dict = {'camelCaseKey': 'value', 'tags': ['tag1', 'tag2'], 'anotherCamelCaseKey': {'nestedCamelCase': 'nestedValue'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict, ignore_list=ignore_list)
    assert snake_dict == {'camel_case_key': 'value', 'tags': ['tag1', 'tag2'], 'another_camel_case_key': {'nested_camel_case': 'nestedValue'}}

def test_camel_dict_to_snake_dict_all_parameters():
    # With all parameters combined
    ignore_list = ('tags',)
    camel_dict = {'camelCaseKey': 'value', 'tags': ['tag1', 'tag2'], 'anotherCamelCaseKey': {'nestedCamelCase': 'nestedValue'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict, reversible=True, ignore_list=ignore_list)
    assert snake_dict == {'camel_case_key': 'value', 'tags': ['tag1', 'tag2'], 'another_camel_case_key': {'nested_camel_case': 'nestedValue'}}

# Additional test cases for uncovered lines
def test_value_is_list():
    # Test the value_is_list function which is not covered by existing tests
    camel_list = [1, {'nestedCamelCase': 2}, [3]]
    snake_list = camel_dict_to_snake_dict({'camelList': camel_list})['camel_list']
    assert isinstance(snake_list[0], int)
    assert isinstance(snake_list[1], dict)
    assert isinstance(snake_list[2], list)

def test_empty_dictionary():
    # Test handling of an empty dictionary
    camel_dict = {}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {}

def test_list_with_mixed_types():
    # Test handling of a list with mixed types
    camel_dict = {'mixedList': [1, {'nestedCamelCase': 2}, 'string']}
    snake_dict = camel_dict_to_snake_dict(camel_dict)['mixed_list']
    assert isinstance(snake_dict[0], int)
    assert isinstance(snake_dict[1], dict)
    assert isinstance(snake_dict[2], str)

def test_deeply_nested_structure():
    # Test handling of a deeply nested structure
    camel_dict = {'deepNested': {'level1': {'level2': {'level3': 'value'}}}}
    snake_dict = camel_dict_to_snake_dict(camel_dict)['deep_nested']['level1']['level2']
    assert snake_dict == {'level3': 'value'}
