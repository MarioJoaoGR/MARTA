
import pytest
from ansible.playbook.base import _generic_g_parent

class MyClass:
    def __init__(self):
        self._squashed = False
        self._finalized = False
        self._attributes = {'name': 'BaseProperty'}
        self._attr_defaults = {'name': 'BaseProperty'}

    def _get_parent_attribute(self, prop_name):
        return getattr(super(), prop_name, None)

class BaseClass:
    pass


def test_invalid_input_none():
    with pytest.raises(AttributeError):
        _generic_g_parent('name', None)