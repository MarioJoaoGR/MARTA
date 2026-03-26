
from pymonet.either import Left, Right  # Correctly importing from pymonet.either
import pytest

def test_valid_input():
    left = Left()
    assert left.is_right() == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_is_right_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Left_is_right_0_test_valid_input.py:6:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""