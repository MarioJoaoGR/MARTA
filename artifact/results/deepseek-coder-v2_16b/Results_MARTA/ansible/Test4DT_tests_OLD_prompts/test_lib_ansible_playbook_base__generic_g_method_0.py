
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.base import _generic_g_method

class MyClassNoProperty:
    def __init__(self):
        self._squashed = False
        self._attributes = {}

class MyClassWithProperty(MyClassNoProperty):
    def __init__(self):
        super().__init__()
        self._attributes['my_property'] = 42
    
    def _get_attr_my_property(self):
        return self._attributes['my_property']


def test_squashed_object():
    obj = MyClassWithProperty()
    value = _generic_g_method('my_property', obj)
    assert value == 42

def test_non_squashed_object():
    obj = MyClassWithProperty()
    with patch.object(obj, '_get_attr_my_property', return_value=42):
        value = _generic_g_method('my_property', obj)
        assert value == 42