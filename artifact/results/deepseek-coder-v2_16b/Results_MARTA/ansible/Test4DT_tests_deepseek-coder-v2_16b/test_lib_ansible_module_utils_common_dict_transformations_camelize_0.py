
import pytest
from your_module import camelize  # Replace 'your_module' with the actual module name where camelize is defined

# Test scenario 1: Valid input - dictionary
def test_valid_input_dict():
    complex_type = {'some_key': 'value'}
    expected_output = {'someKey': 'value'}
    assert camelize(complex_type) == expected_output

# Test scenario 2: Valid input - list of dictionaries
def test_valid_input_list():
    complex_type = [{'another_key': 'example'}, {'yet_another_key': 'test'}]
    expected_output = [{'anotherKey': 'example'}, {'yetAnotherKey': 'test'}]
    assert camelize(complex_type) == expected_output

# Test scenario 3: Invalid input - string that is not a dict or list
def test_invalid_input_string():
    complex_type = 'not_a_dict_or_list'
    expected_output = 'not_a_dict_or_list'
    assert camelize(complex_type) == expected_output
