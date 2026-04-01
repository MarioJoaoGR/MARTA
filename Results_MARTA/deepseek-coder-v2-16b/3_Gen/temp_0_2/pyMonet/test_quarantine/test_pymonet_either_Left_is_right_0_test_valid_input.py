
from pymonet.either import Left

def test_valid_input():
    left = Left()
    assert not left.is_right(), "Expected is_right() to return False for a valid instance of Left"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_is_right_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Left_is_right_0_test_valid_input.py:5:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""