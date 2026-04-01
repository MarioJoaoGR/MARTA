
from pymonet.validation import Validation
from pymonet.either import Left, Right
import pytest

def test_valid_input():
    # Create a valid Validation instance
    val = Validation(10, [])
    
    # Convert to Either and check the result
    either_val = val.to_either()
    
    # Assert that it is a Right with the correct value
    assert isinstance(either_val, Right)
    assert either_val.get_value() == 10

def test_invalid_input():
    # Create an invalid Validation instance
    val = Validation(None, ["Error message"])
    
    # Convert to Either and check the result
    either_val = val.to_either()
    
    # Assert that it is a Left with the correct errors
    assert isinstance(either_val, Left)
    assert either_val.get_error() == ["Error message"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_either_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_valid_input.py:15:11: E1101: Instance of 'Right' has no 'get_value' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_valid_input.py:15:11: E1101: Instance of 'Left' has no 'get_value' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_valid_input.py:26:11: E1101: Instance of 'Right' has no 'get_error' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_valid_input.py:26:11: E1101: Instance of 'Left' has no 'get_error' member (no-member)


"""