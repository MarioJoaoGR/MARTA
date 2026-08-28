
# Module: ansible.playbook.base
from ansible.playbook.base import _generic_g_method

def test_generic_g_method_with_existing_property():
    class TestClass:
        def __init__(self):
            self._squashed = True
            self._attributes = {'my_property': 'value'}
        
        def _get_attr_my_property(self):
            return self._attributes['my_property']
    
    obj = TestClass()
    assert _generic_g_method('my_property', obj) == 'value'

def test_generic_g_method_with_non_existing_property():
    class TestClass:
        def __init__(self):
            self._squashed = True
            self._attributes = {}
        
        def _get_attr_my_property(self):
            raise AttributeError("This method should not be called.")
    
    obj = TestClass()
    try:
        result = _generic_g_method('my_property', obj)
    except AttributeError as e:
        assert str(e) == "'%s' object has no attribute '%s'" % (obj.__class__.__name__, 'my_property')
    else:
        assert False, "Expected AttributeError was not raised."

def test_generic_g_method_with_squashed_false():
    class TestClass:
        def __init__(self):
            self._squashed = False
            self._attributes = {'my_property': 'value'}
        
        def _get_attr_my_property(self):
            return self._attributes['my_property']
    
    obj = TestClass()
    assert _generic_g_method('my_property', obj) == 'value'

def test_generic_g_method_with_squashed_true_and_no_method():
    class TestClass:
        def __init__(self):
            self._squashed = True
            self._attributes = {'my_property': 'value'}
        
        def _get_attr_my_property(self):
            raise AttributeError("This method should not be called.")
    
    obj = TestClass()
    try:
        _generic_g_method('my_property', obj)
    except AttributeError as e:
        assert str(e) == "'%s' object has no attribute '%s'" % (obj.__class__.__name__, 'my_property')
    else:
        assert False, "Expected AttributeError was not raised."
