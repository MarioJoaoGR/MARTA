
import pytest
from pytutils.excs import InvalidInputError

def test_invalid_inputs():
    # Test that it passes through specified exceptions
    with pytest.raises(ZeroDivisionError):
        with ok(ZeroDivisionError):
            raise ZeroDivisionError("Test division by zero")

    # Test that other exceptions are reraised
    with pytest.raises(ValueError):
        with ok():
            raise ValueError("Test exception")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_excs_ok_7_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_excs_ok_7_test_invalid_inputs.py:3:0: E0611: No name 'InvalidInputError' in module 'pytutils.excs' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_excs_ok_7_test_invalid_inputs.py:8:13: E0602: Undefined variable 'ok' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_excs_ok_7_test_invalid_inputs.py:13:13: E0602: Undefined variable 'ok' (undefined-variable)


"""