
import pytest
from pytutils.memo import CachedException

def test_valid_input():
    class CustomError(Exception):
        pass
    
    ex = CustomError("An error occurred")
    cached_exception = CachedException(ex)
    
    with pytest.raises(CustomError) as excinfo:
        raise cached_exception
    
    assert isinstance(excinfo.value, CustomError)
    assert str(excinfo.value) == "An error occurred"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo_CachedException___init___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_memo_CachedException___init___0_test_valid_input.py:13:8: E0710: Raising a class which doesn't inherit from BaseException (raising-non-exception)


"""