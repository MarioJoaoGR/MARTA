
import pytest
from ansible.playbook.base import _generic_s

def test_set_property():
    class MyClass:
        def __init__(self):
            self._attributes = {}
    
    obj = MyClass()
    prop_name = 'my_property'
    value = 'some_value'
    
    _generic_s(prop_name, obj, value)
    
    assert obj._attributes == {prop_name: value}

def test_set_different_property():
    class AnotherClass:
        def __init__(self):
            self._attributes = {}
    
    another_obj = AnotherClass()
    prop_name = 'another_property'
    value = 'different_value'
    
    _generic_s(prop_name, another_obj, value)
    
    assert another_obj._attributes == {prop_name: value}

def test_set_default_property():
    class YetAnotherClass:
        def __init__(self):
            self._attributes = {}
    
    yet_another_obj = YetAnotherClass()
    prop_name = 'yet_another_property'
    value = 'default_value'
    
    _generic_s(prop_name, yet_another_obj, value)
    
    assert yet_another_obj._attributes == {prop_name: value}
