
import pytest
from flutes.exception import UnwrapException

def _unwrap(fn):
    """
    Recursively unwraps a function to get the original wrapped function.
    
    This function takes a callable (function) as an argument and returns the underlying, unwrapped function.
    If the provided callable has a `__wrapped__` attribute, it will recursively call itself with this attribute until no more wrapping is found.
    
    Parameters:
        fn (callable): The function to be unwrapped. It should be a Python callable object such as a function or method.
        
    Returns:
        callable: The original, unwrapped function.
        
    Examples:
        >>> def wrapped_func():
        ...     return "Wrapped!"
        ... 
        >>> wrapped_func = some_decorator(wrapped_func)
        >>> print(_unwrap(wrapped_func))
        <function some_decorator.<locals>.wrapper at 0x...>
        
        >>> def another_func():
        ...     return "Unwrapped!"
        ... 
        >>> print(_unwrap(another_func))
        <function another_func at 0x...>
    """
    if hasattr(fn, "__wrapped__"):
        return _unwrap(fn.__wrapped__)
    return fn

def test_wrapped_function():
    def wrapped_func():
        return "Wrapped!"
    
    # Mocking a decorator to wrap the function
    def mock_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    wrapped_func = mock_decorator(wrapped_func)
    
    # Unwrapping the function
    unwrapped_func = _unwrap(wrapped_func)
    
    # Assert that the original function is returned after unwrapping
    assert unwrapped_func == wrapped_func.__wrapped__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception__unwrap_0_test_wrapped_function
flutes/Test4DT_tests/test_flutes_exception__unwrap_0_test_wrapped_function.py:3:0: E0611: No name 'UnwrapException' in module 'flutes.exception' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_exception__unwrap_0_test_wrapped_function.py:52:29: E1101: Function 'wrapper' has no '__wrapped__' member (no-member)


"""