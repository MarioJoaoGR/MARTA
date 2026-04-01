
from pymonet.either import Left, Right

def test_error_handling():
    left = Left()
    assert not left.is_right(), "Expected is_right to return False for a Left instance"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_is_right_0_test_error_handling
pyMonet/Test4DT_tests/test_pymonet_either_Left_is_right_0_test_error_handling.py:5:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""