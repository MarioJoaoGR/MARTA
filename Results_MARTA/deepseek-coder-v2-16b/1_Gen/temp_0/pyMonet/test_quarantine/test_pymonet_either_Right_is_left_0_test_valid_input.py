
from pymonet.either import Right

def test_valid_input():
    right_value = Right()
    assert not right_value.is_left(), "Expected is_left to return False"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_is_left_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Right_is_left_0_test_valid_input.py:5:18: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""