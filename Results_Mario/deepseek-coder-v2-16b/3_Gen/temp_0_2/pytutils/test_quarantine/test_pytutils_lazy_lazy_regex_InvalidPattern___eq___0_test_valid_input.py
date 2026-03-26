
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_valid_input():
    # Arrange
    msg = "This is a valid message"
    
    # Act
    try:
        raise InvalidPattern(msg)
    except InvalidPattern as e:
        pass  # We just want to check if the exception was raised correctly
    
    # Assert
    assert isinstance(e, InvalidPattern)
    assert e.msg == msg

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_InvalidPattern___eq___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_InvalidPattern___eq___0_test_valid_input.py:16:22: E0601: Using variable 'e' before assignment (used-before-assignment)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_InvalidPattern___eq___0_test_valid_input.py:17:11: E0601: Using variable 'e' before assignment (used-before-assignment)


"""