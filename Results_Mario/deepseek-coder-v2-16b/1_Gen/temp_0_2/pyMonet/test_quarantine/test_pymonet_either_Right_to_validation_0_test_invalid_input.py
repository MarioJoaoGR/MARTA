
import pytest
from pymonet.either import Right

def test_invalid_input():
    right_instance = Right()
    with pytest.raises(AttributeError):
        validated = right_instance.to_validation()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_to_validation_0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_either_Right_to_validation_0_test_invalid_input.py:6:21: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""