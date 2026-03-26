
import pytest
from flutes.exception import decorator

def log_exception(e):
    print(f"An exception occurred: {e}")

@decorator
def safe_function():
    raise ValueError("Example error")

def test_valid_input():
    with pytest.raises(ValueError) as exc_info:
        safe_function()
    assert str(exc_info.value) == "Example error"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_decorator_0_test_valid_input
flutes/Test4DT_tests/test_flutes_exception_decorator_0_test_valid_input.py:3:0: E0611: No name 'decorator' in module 'flutes.exception' (no-name-in-module)

"""