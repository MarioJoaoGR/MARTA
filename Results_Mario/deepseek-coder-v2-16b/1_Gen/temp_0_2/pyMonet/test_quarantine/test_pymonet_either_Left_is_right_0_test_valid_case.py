
from pymonet.either import Left
import pytest

def test_valid_case():
    left_instance = Left()
    assert not left_instance.is_right(), "Expected is_right to return False"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_is_right_0_test_valid_case
pyMonet/Test4DT_tests/test_pymonet_either_Left_is_right_0_test_valid_case.py:6:20: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""