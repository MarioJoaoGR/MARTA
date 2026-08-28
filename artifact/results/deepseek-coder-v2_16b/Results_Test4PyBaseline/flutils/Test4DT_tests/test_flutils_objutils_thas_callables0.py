# Module: flutils.objutils
import pytest
from flutils.objutils import has_callables
from typing import Any as _Any

# Helper function to check if attributes exist on an object
def has_attrs(obj, *attrs):
    for attr in attrs:
        if not hasattr(obj, attr):
            return False
    return True

# Test cases for has_callables function

# Basic Usage: Check if a dictionary has methods 'get', 'keys', 'items', and 'values'
def test_has_callables_basic():
    result = has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert result is True, "Expected True for basic usage with a dictionary"

# Check with Different Object: Custom object with method 'my_method'
class CustomObject:
    def my_method(self):
        pass

def test_has_callables_custom_object():
    obj = CustomObject()
    result = has_callables(obj, 'my_method')
    assert result is True, "Expected True for custom object with callable method"

# Check with Non-Callable Attributes: Check if a dictionary does not have a non-existent attribute
def test_has_callables_non_existent_attribute():
    result = has_callables(dict(), 'non_existent_method')
    assert result is False, "Expected False for non-existent attribute"

# Using with Different Object Types: Check if a list object has method 'append'
def test_has_callables_list_object():
    result = has_callables([], 'append')
    assert result is True, "Expected True for list object with callable method"

# Edge Case with None: Check if `None` has any attributes (which it should not)
def test_has_callables_none():
    result = has_callables(None, 'any_attribute')
    assert result is False, "Expected False for None object"
