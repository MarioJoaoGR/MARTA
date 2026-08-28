
import pytest
from unittest.mock import MagicMock

# Assuming Sentinel is defined somewhere in the module or globally
Sentinel = object()

def _generic_g(prop_name, instance):
    if hasattr(instance, '_attributes') and prop_name in instance._attributes:
        return instance._attributes[prop_name]
    elif hasattr(instance, '_attr_defaults') and prop_name in instance._attr_defaults:
        return instance._attr_defaults[prop_name]
    else:
        raise AttributeError(f"'{type(instance).__name__}' object has no attribute '{prop_name}'")

def test_retrieve_property_from_attributes():
    class MyClass:
        def __init__(self):
            self._attributes = {'prop1': 1, 'prop2': Sentinel}
            self._attr_defaults = {'prop1': 0, 'prop2': 2}
    
    obj = MyClass()
    assert _generic_g('prop1', obj) == 1
    assert _generic_g('prop2', obj) == 2

def test_retrieve_property_from_defaults():
    class MyClass:
        def __init__(self):
            self._attributes = {'prop1': 1}
            self._attr_defaults = {'prop1': 0, 'prop2': 2}
    
    obj = MyClass()
    assert _generic_g('prop2', obj) == 2

def test_raise_attribute_error():
    class MyClass:
        def __init__(self):
            self._attributes = {'prop1': 1}
            self._attr_defaults = {'prop1': 0}
    
    obj = MyClass()
    with pytest.raises(AttributeError) as e:
        _generic_g('prop2', obj)
    assert str(e.value) == "'MyClass' object has no attribute 'prop2'"

def test_static_method():
    class MyClass:
        @staticmethod
        def get_property(prop_name, instance):
            return _generic_g(prop_name, instance)
    
    obj = MyClass()
    assert MyClass.get_property('prop1', obj) == 1
    assert MyClass.get_property('prop2', obj) == 2
