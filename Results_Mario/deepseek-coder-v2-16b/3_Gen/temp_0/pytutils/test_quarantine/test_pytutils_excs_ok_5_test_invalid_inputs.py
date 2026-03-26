
import pytest
from pytutils.excs import InvalidInputError

def ok(*exceptions):
    """Context manager to pass exceptions.
    :param exceptions: Exceptions to pass
    """
    try:
        yield
    except Exception as e:
        if isinstance(e, exceptions):
            pass
        else:
            raise e

# Test case for invalid inputs
def test_invalid_inputs():
    with pytest.raises(InvalidInputError):
        with ok(ZeroDivisionError):
            print(1 / 0)  # This will not raise an error because ZeroDivisionError is passed.

    try:
        with ok():
            raise ValueError("Test exception")
    except ValueError as e:
        assert str(e) == "Test exception"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_excs_ok_5_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_excs_ok_5_test_invalid_inputs.py:3:0: E0611: No name 'InvalidInputError' in module 'pytutils.excs' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_excs_ok_5_test_invalid_inputs.py:20:8: E1129: Context manager 'generator' doesn't implement __enter__ and __exit__. (not-context-manager)
pytutils/Test4DT_tests/test_pytutils_excs_ok_5_test_invalid_inputs.py:24:8: E1129: Context manager 'generator' doesn't implement __enter__ and __exit__. (not-context-manager)


"""