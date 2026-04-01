
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

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        with ok(InvalidInputError):
            raise InvalidInputError("Test invalid input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_excs_ok_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_excs_ok_0_test_invalid_input.py:3:0: E0611: No name 'InvalidInputError' in module 'pytutils.excs' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_excs_ok_0_test_invalid_input.py:19:8: E1129: Context manager 'generator' doesn't implement __enter__ and __exit__. (not-context-manager)


"""