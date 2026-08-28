# Module: flutils.objutils
import pytest
from flutils.objutils import has_any_callables
from typing import Any as _Any

# Helper function to check if any of the given attributes exist on the object
def has_any_attrs(obj, *attrs):
    return any(hasattr(obj, attr) for attr in attrs)

# Test cases for has_any_callables function

# Basic Usage: Checking if an object has any callable attributes among a list of specified attribute names.
def test_basic_usage():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True

# No Callable Attributes: Checking if an object does not have any callable attributes among a list of specified attribute names.
def test_no_callable_attributes():
    assert has_any_callables(dict(), 'foo', 'bar') is False

# Object with Callable Attributes: Checking if a custom object has any callable attributes among a list of specified attribute names.
class CustomObj:
    def method1(self):
        pass
    
    def method2(self):
        pass

def test_object_with_callable_attributes():
    custom_obj = CustomObj()
    assert has_any_callables(custom_obj, 'method1', 'method2', 'non_existent_attr') is True

# Non-Callable Attributes: Checking if a custom object has any callable attributes among a list of specified attribute names, where some attributes do not exist on the object.
def test_non_callable_attributes():
    class CustomObj:
        def method1(self):
            pass
        
        def method2(self):
            pass
    
    custom_obj = CustomObj()
    assert has_any_callables(custom_obj, 'method1', 'method2', 'non_existent_attr') is True

# Edge Case with None: Checking if an object has any callable attributes among a list of specified attribute names when the object is `None`.
def test_none():
    assert has_any_callables(None, 'get', 'keys', 'items', 'values') is False
