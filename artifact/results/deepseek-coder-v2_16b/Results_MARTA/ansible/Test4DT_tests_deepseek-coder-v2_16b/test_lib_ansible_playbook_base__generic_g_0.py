
import pytest
from ansible.playbook.base import _generic_g

class MyClass:
    def __init__(self):
        self._attributes = {'prop1': 1, 'prop2': 2}
        self._attr_defaults = {'prop1': 0, 'prop3': 3}

class AnotherClass:
    def __init__(self):
        self._attributes = {'propA': 'valueA', 'propB': 'valueB'}
        self._attr_defaults = {'propA': 'defaultA', 'propC': 'defaultC'}

def test_valid_case_1():
    obj = MyClass()
    assert _generic_g('prop1', obj) == 1

def test_valid_case_2():
    obj = AnotherClass()
    assert _generic_g('propA', obj) == 'valueA'

def test_error_case():
    obj = MyClass()
    with pytest.raises(AttributeError):
        _generic_g('prop3', obj)
