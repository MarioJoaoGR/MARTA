
import pytest
from flutes.exception import SomeException  # Assuming SomeException is defined in flutes.exception module

def _unwrap(fn):
    """
    Recursively unwraps a function to get the original function it was wrapped with.
    
    This function is used internally by other parts of the codebase to access the original, unwrapped version of a function.
    
    Parameters:
        fn (function): The function to be unwrapped.
        
    Returns:
        function: The original, unwrapped function.
        
    Example:
        To use this function, you would call it with a wrapped function as the argument. For example:
        
        def my_function():
            pass
        
        # Suppose `my_function` is wrapped by some other code
        original_fn = _unwrap(my_function)
        print(original_fn.__name__)  # This would print 'my_function' if no wrappers are present.
    """
    def _unwrap(fn):
        if hasattr(fn, "__wrapped__"):
            return _unwrap(fn.__wrapped__)
        return fn

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception__unwrap_0_test_valid_input
flutes/Test4DT_tests/test_flutes_exception__unwrap_0_test_valid_input.py:3:0: E0611: No name 'SomeException' in module 'flutes.exception' (no-name-in-module)


"""