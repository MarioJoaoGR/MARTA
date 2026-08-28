
import pytest
from ansible.playbook.base import _generic_g_method

def test_valid_squashed_input():
    class MyClass:
        def __init__(self):
            self._attributes = {'my_property': 42}
            self._squashed = True
    
    obj = MyClass()
    assert _generic_g_method('my_property', obj) == 42

def test_valid_non_squashed_input():
    class MyClass:
        def __init__(self):
            self._attributes = {'my_property': 42}
            self._squashed = False
    
        def _get_attr_my_property(self):
            return self._attributes['my_property']
    
    obj = MyClass()
    assert _generic_g_method('my_property', obj) == 42

def test_invalid_input():
    class MyClass:
        def __init__(self):
            self._attributes = {'my_other_property': 42}
            self._squashed = False
    
        def _get_attr_my_property(self):
            raise AttributeError("No such attribute")
    
    obj = MyClass()
    with pytest.raises(AttributeError) as excinfo:
        _generic_g_method('my_property', obj)
