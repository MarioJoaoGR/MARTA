
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