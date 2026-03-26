
import pytest
from subprocess import CalledProcessError
from flutes.run import error_wrapper

def test_valid_input():
    try:
        result = subprocess.run(['ls', '-l', '/nonexistent_file'], check=True, capture_output=True)
    except Exception as e:
        wrapped_e = error_wrapper(e)
        assert "No such file or directory" in str(wrapped_e)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_run_error_wrapper_0_test_valid_input
flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_valid_input.py:8:17: E0602: Undefined variable 'subprocess' (undefined-variable)

"""