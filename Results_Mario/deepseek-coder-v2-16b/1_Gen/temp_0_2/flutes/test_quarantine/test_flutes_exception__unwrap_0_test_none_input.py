
import pytest
from flutes.exception import InvalidInputError

def _unwrap(fn):
    """
    Recursively unwraps a function to get the original function that was wrapped.
    
    This function checks if the provided object has a `__wrapped__` attribute, which is typical for functions wrapped by certain libraries like functools.wraps. If such an attribute exists, it recursively calls itself with the wrapped function until the original function is reached.
    
    Parameters:
        fn (function): The function to unwrap. It should be a callable object that has a `__wrapped__` attribute if it's been wrapped by another function.
        
    Returns:
        function: The original, unwrapped function.
        
    Examples:
        >>> def example_function():
        ...     print("This is the original function.")
        ... 
        >>> # Wrapping the function for demonstration purposes
        >>> import functools
        >>> wrapped_example = functools.wraps(example_function)(example_function)
        >>> 
        >>> # Now unwrapping to get back the original function
        >>> original_example = _unwrap(wrapped_example)
        >>> original_example()
        This is the original function.
        
    Note:
        This function assumes that the provided callable has a `__wrapped__` attribute if it's been wrapped by another function, which is common in Python when using decorators like those from functools. If you use this function with non-decorator wrapped functions or objects without a `__wrapped__` attribute, it will return the object itself.
    
    Internally used by Flutes for retrieving the underlying function from decorator chains.
    
    Parameters:
        fn (callable): The function to be unwrapped.
        
    Returns:
        callable: The original function before any decorators were applied.
    """
    def _unwrap(fn):
        if hasattr(fn, "__wrapped__"):
            return _unwrap(fn.__wrapped__)
        return fn

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception__unwrap_0_test_none_input
flutes/Test4DT_tests/test_flutes_exception__unwrap_0_test_none_input.py:3:0: E0611: No name 'InvalidInputError' in module 'flutes.exception' (no-name-in-module)


"""