
# flutes/Test4DT_tests/test_flutes_exception__unwrap_0_test_none_input.py
import pytest
from flutes.exception import SomeException

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

def test_none_input():
    # Test that _unwrap handles None input gracefully
    with pytest.raises(TypeError):
        assert _unwrap(None) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception__unwrap_0_test_none_input
flutes/Test4DT_tests/test_flutes_exception__unwrap_0_test_none_input.py:4:0: E0611: No name 'SomeException' in module 'flutes.exception' (no-name-in-module)


"""