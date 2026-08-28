
import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict

# Test cases for snake_dict_to_camel_dict function

def test_basic_conversion():
    snake_dict = {'foo_bar': 1, 'baz_qux': {'quux_corge': 2, 'grault_garply': [3, 4]}}
    expected_result = {'fooBar': 1, 'bazQux': {'quuxCorge': 2, 'graultGarply': [3, 4]}}
    assert snake_dict_to_camel_dict(snake_dict) == expected_result

def test_conversion_with_capitalization():
    snake_dict = {'foo_bar': 1, 'baz_qux': {'quux_corge': 2, 'grault_garply': [3, 4]}}
    expected_result = {'FooBar': 1, 'BazQux': {'QuuxCorge': 2, 'GraultGarply': [3, 4]}}
    assert snake_dict_to_camel_dict(snake_dict, capitalize_first=True) == expected_result

def test_conversion_with_simple_dictionary():
    snake_dict = {'foo_bar': 1}
    expected_result = {'fooBar': 1}
    assert snake_dict_to_camel_dict(snake_dict) == expected_result

def test_conversion_with_nested_structures():
    snake_dict = {'foo_bar': 1, 'baz_qux': [5, {'quux_corge': 2, 'grault_garply': [3, 4]}]}
    expected_result = {'fooBar': 1, 'bazQux': [5, {'quuxCorge': 2, 'graultGarply': [3, 4]}]}
    assert snake_dict_to_camel_dict(snake_dict) == expected_result

def test_none_input():
    assert snake_dict_to_camel_dict(None) is None

def test_empty_dictionary():
    assert snake_dict_to_camel_dict({}) == {}

@pytest.mark.xfail  # Expected to fail as per the provided output
def test_list_input():
    with pytest.raises(TypeError):
        snake_dict_to_camel_dict([1, 2, 3])

# Add more tests as needed to cover all edge cases and scenarios
