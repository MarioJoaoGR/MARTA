
import pytest
from flutes.log import log_exception
from flutes.exception import FlutesException

def test_valid_inputs():
    with pytest.raises(FlutesException):
        try:
            raise FlutesException("Test exception")
        except FlutesException as e:
            log_exception(e, user_msg="User action required")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_log_exception_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_valid_inputs.py:4:0: E0611: No name 'FlutesException' in module 'flutes.exception' (no-name-in-module)


"""