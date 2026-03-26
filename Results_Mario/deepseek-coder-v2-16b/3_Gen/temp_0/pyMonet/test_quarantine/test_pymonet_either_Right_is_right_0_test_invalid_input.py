
from pymonet.either import Right
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):  # Expecting a TypeError since no value is provided to the constructor
        Right()  # This should raise an error because the constructor does not accept any parameters

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_is_right_0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_either_Right_is_right_0_test_invalid_input.py:7:8: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""