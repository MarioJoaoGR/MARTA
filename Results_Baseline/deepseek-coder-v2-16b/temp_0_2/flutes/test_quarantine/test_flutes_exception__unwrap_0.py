
# Module: flutes.exception
import pytest
from flutes.exception import _unwrap

# Test cases for the _unwrap function

def test_unwrapping_non_wrapped_function():
    def original_function():
        return "This is an unwrapped function."
    
    wrapped_example = _unwrap(original_function)
    
    assert wrapped_example() == "This is an unwrapped function."

def test_unwrapping_wrapped_function():
    def original_function():
        return "This is the original function."
    
    def wrapper_function(fn):
        fn.__wrapped__ = original_function
        return fn
    
    wrapped_func = wrapper_function(original_function)
    
    unwrapped_func = _unwrap(wrapped_func)
    assert unwrapped_func() == "This is the original function."

def test_unwrapping_function_with_multiple_wrappers():
    def original_function():
        return "This is the original function."
    
    def first_wrapper(fn):
        fn.__wrapped__ = original_function
        return fn
    
    def second_wrapper(fn):
        fn.__wrapped__ = first_wrapper
        return fn
    
    wrapped_func = second_wrapper(original_function)
    
    unwrapped_func = _unwrap(wrapped_func)
    assert unwrapped_func() == "This is the original function."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception__unwrap_0
flutes/Test4DT_tests/test_flutes_exception__unwrap_0.py:4:0: E0611: No name '_unwrap' in module 'flutes.exception' (no-name-in-module)


"""