
import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_valid_input():
    # Call the function to get the namespace
    namespace = _namespace_from_calling_context()
    
    # Check that it returns a string (fully qualified Python name of a module)
    assert isinstance(namespace, str), "The returned value is not a string."
    
    # Check that the returned namespace matches what we expect from the current call stack
    expected_namespace = inspect.stack()[1][0].f_globals["__name__"]
    assert namespace == expected_namespace, f"Expected {expected_namespace}, but got {namespace}"
