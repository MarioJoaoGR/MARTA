
import pytest
from flutes.exception import WrappedException

def test_valid_input():
    def func():
        return "test"
    
    wrapped_func = wrapped(func)
    assert wrapped_func() == "test"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_wrapped_0_test_valid_input
flutes/Test4DT_tests/test_flutes_exception_wrapped_0_test_valid_input.py:3:0: E0611: No name 'WrappedException' in module 'flutes.exception' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_exception_wrapped_0_test_valid_input.py:9:19: E0602: Undefined variable 'wrapped' (undefined-variable)


"""