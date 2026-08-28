
import pytest
from apimd.parser import _e_type

class Constant:
    def __init__(self, value):
        self.value = value


def test_mixed_elements():
    class MyClass: pass
    my_obj = MyClass()
    assert _e_type([my_obj, Constant(1)]) == ''

def test_empty_list():
    assert _e_type([]) == ''

def test_none_elements():
    assert _e_type([None]) == ''