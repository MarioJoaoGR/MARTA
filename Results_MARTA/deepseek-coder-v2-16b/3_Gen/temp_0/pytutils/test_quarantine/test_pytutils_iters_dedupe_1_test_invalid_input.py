
import pytest
from pytutils.iters import dedupe

def test_invalid_input():
    # Define a function that returns an invalid input (e.g., not iterable)
    def invalid_func():
        return 123
    
    # Use the dedupe decorator with the invalid function
    with pytest.raises(TypeError):
        # Apply the dedupe decorator to an invalid function
        decorated_invalid_func = dedupe(invalid_func, instance=None, args=(), kwargs={})
        list(decorated_invalid_func())  # This should raise a TypeError if the output is not iterable

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_iters_dedupe_1_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_invalid_input.py:14:13: E1102: decorated_invalid_func is not callable (not-callable)


"""