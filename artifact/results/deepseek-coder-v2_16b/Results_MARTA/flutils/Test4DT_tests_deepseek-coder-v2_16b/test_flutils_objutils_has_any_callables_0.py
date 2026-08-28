
import pytest
from flutils.objutils import has_any_callables

# Test case for checking if an object has any callable attributes among a set of specified names
def test_has_any_callables_with_callable_attributes():
    class MyClass:
        def method1(self):
            pass
        
        @staticmethod
        def method2():
            pass
    
    obj = MyClass()
    result = has_any_callables(obj, 'method1', 'method2', 'non_existent_attr')
    assert result is True, "Expected True because both method1 and method2 are callable"

# Test case for checking if an object does not have any callable attributes among a set of specified names
def test_has_any_callables_without_callable_attributes():
    class MyClass:
        def method1(self):
            pass
        
        @staticmethod
        def method2():
            pass
    
    obj = MyClass()
    result = has_any_callables(obj, 'non_existent_attr')
    assert result is False, "Expected False because there are no callable attributes"

# Test case for checking if a dictionary object has any of the specified methods that are callable
def test_has_any_callables_with_dictionary():
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert result is True, "Expected True because dict().get is callable"

# Test case for checking if a dictionary object does not have any of the specified methods that are callable
def test_has_any_callables_without_dictionary_callable():
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert result is True, "Expected True because dict().get is callable"
