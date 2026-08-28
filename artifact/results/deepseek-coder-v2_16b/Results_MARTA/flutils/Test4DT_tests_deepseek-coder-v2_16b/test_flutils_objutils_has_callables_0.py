
import pytest
from flutils.objutils import has_callables

# Test case for checking if an object has all callable attributes
def test_has_all_callable_attributes():
    class CallableClass:
        def method1(self):
            pass
        
        @staticmethod
        def method2():
            pass
    
    instance = CallableClass()
    assert has_callables(instance, 'method1', 'method2') is True

# Test case for checking if an object does not have callable attributes
def test_no_callable_attributes():
    class NoCallable:
        def __init__(self):
            self.attr1 = "value"
            self.attr2 = 42
    
    instance = NoCallable()
    assert has_callables(instance, 'attr1', 'attr2') is False

# Test case for checking if an object has one callable and one non-callable attribute
def test_mixed_attributes():
    class MixedAttributes:
        def method(self):
            pass
    
    instance = MixedAttributes()
    assert has_callables(instance, 'method', 'non_existent_attr') is False

# Test case for checking if built-in types have callable attributes
def test_builtin_types():
    assert has_callables(dict(), 'get', 'keys') is True

# Edge case: empty object and no attributes
def test_empty_object():
    class EmptyClass:
        pass
    
    instance = EmptyClass()
    assert has_callables(instance, 'non_existent_attr') is False
