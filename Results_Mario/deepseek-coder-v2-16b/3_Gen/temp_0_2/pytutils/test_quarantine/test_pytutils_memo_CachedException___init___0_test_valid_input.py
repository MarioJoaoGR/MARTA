
import pytest
from pytutils.memo import CachedException

def test_valid_input():
    ex = ValueError("Invalid value")
    exception_instance = CachedException(ex)
    with pytest.raises(ValueError) as exc_info:
        raise exception_instance
    assert str(exc_info.value) == "Invalid value"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo_CachedException___init___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_memo_CachedException___init___0_test_valid_input.py:9:8: E0710: Raising a class which doesn't inherit from BaseException (raising-non-exception)


"""