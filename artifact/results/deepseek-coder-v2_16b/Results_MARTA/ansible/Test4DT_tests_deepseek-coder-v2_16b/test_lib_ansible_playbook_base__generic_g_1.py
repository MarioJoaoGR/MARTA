
import pytest
from ansible.playbook.base import _generic_g

class NonStringClass:
    def __init__(self):
        self._attributes = {'prop1': 1, 'prop2': 2}
        self._attr_defaults = {'prop1': 0, 'prop3': 3}

def test_valid_input():
    obj = NonStringClass()
    assert _generic_g('prop1', obj) == 1
    assert _generic_g('prop2', obj) == 2

def test_invalid_input():
    obj = NonStringClass()
    with pytest.raises(AttributeError):
        _generic_g('prop3', obj)
