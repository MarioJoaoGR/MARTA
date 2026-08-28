
import pytest
from apimd.parser import _e_type, Constant


def test_contains_non_constant_types():
    class MyClass: pass
    my_obj = MyClass()
    
    elements = [my_obj, Constant(1)]
    assert _e_type(elements) == ''

def test_empty_list():
    assert _e_type([]) == ''

def test_list_with_none():
    assert _e_type([None]) == ''