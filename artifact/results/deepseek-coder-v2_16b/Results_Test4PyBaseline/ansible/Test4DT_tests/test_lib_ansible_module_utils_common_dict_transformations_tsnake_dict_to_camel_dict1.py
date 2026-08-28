
import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict, _snake_to_camel

# Test cases for camelize function within snake_dict_to_camel_dict

def test_camelize_basic():
    assert snake_dict_to_camel_dict({'foo_bar': 1}) == {'fooBar': 1}

def test_camelize_nested():
    nested_dict = {'foo_bar': 1, 'baz_qux': {'quux_corge': 2}}
    expected_result = {'fooBar': 1, 'bazQux': {'quuxCorge': 2}}
    assert snake_dict_to_camel_dict(nested_dict) == expected_result

def test_camelize_list():
    list_dict = {'foo_bar': 1, 'baz_qux': [5, {'quux_corge': 2}]}
    expected_result = {'fooBar': 1, 'bazQux': [5, {'quuxCorge': 2}]}