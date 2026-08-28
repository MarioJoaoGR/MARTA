
# Module: ansible.playbook.base
from ansible.playbook.base import _generic_g_method
import pytest

def test_generic_g_method_with_squashed_true_and_no_method():
    class TestClass:
        def __init__(self):
            self._squashed = True
            self._attributes = {'my_property': 'value'}
        
        def _get_attr_my_property(self):
            raise AttributeError("This method should not be called.")
    
    obj = TestClass()
    assert _generic_g_method('my_property', obj) == 'value'

def test_generic_g_method_with_squashed_false_and_no_method():
    class TestClass:
        def __init__(self):
            self._squashed = False
            self._attributes = {'my_property': 'value'}
        
        def _get_attr_my_property(self):
            raise AttributeError("This method should not be called.")
    
    obj = TestClass()
    with pytest.raises(AttributeError) as excinfo:
        _generic_g_method('my_property', obj)