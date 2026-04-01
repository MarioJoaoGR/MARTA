
import pytest
from pytutils.memo import CachedException

class TestCachedExceptionInit:
    def test_valid_input(self):
        with pytest.raises(ValueError) as excinfo:
            ex = ValueError("Example error")
            ce = CachedException(ex)
            raise ce  # This will actually raise the exception stored in `ce`

        assert str(excinfo.value) == "Example error"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo_CachedException___init___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_memo_CachedException___init___0_test_valid_input.py:10:12: E0710: Raising a class which doesn't inherit from BaseException (raising-non-exception)


"""