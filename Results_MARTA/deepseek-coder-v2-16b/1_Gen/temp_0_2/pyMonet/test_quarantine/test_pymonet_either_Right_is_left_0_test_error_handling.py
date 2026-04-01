
from pymonet.either import Right

def test_is_left():
    right = Right()
    assert not right.is_left(), "Expected is_left to return False"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_is_left_0_test_error_handling
pyMonet/Test4DT_tests/test_pymonet_either_Right_is_left_0_test_error_handling.py:5:12: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""