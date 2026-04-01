
import pytest
from pymonet.either import Left

def test_is_left():
    left_instance = Left()
    assert left_instance.is_left() is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_is_left_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_either_Left_is_left_0_test_edge_case.py:6:20: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""