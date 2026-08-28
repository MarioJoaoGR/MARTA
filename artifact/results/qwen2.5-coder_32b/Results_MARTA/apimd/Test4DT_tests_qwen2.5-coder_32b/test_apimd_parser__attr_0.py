
import pytest
from apimd.parser import _attr

def test_invalid_inputs_with_non_string_attribute():
    invalid_obj = 123
    assert _attr(invalid_obj, 'a.b.c') is None

def test_invalid_inputs_with_list_attribute():
    invalid_attr = ['a', 'b']
    assert _attr({}, 'a.b') is None




def test_non_existent_nested_dict_access():
    valid_obj = {'a': {'b': {}}}
    assert _attr(valid_obj, 'a.b.c') is None

def test_non_existent_nested_object_access():
    class Example:
        def __init__(self):
            self.x = {'y': {}}
    
    obj = Example()
    assert _attr(obj, 'x.y.z') is None