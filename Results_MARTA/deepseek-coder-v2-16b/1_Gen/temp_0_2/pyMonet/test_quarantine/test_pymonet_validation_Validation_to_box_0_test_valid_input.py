
from pymonet.validation import Validation
import pytest

def test_valid_input():
    # Create a Validation instance with a valid value
    validation = Validation(10, [])
    
    # Test that has_errors returns False when there are no errors
    assert not validation.has_errors(), "Expected no errors but found some"
    
    # Test that get_value returns the stored value when there are no errors
    assert validation.get_value() == 10, "Expected value to be 10 but got something else"
    
    # Test that to_box returns a Box with the value when there are no errors
    from pymonet.box import Box
    box = validation.to_box()
    assert isinstance(box, Box), "Expected a Box instance"
    assert box.value == 10, "Expected Box to contain the value 10"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_box_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_box_0_test_valid_input.py:10:15: E1101: Instance of 'Validation' has no 'has_errors' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_box_0_test_valid_input.py:13:11: E1101: Instance of 'Validation' has no 'get_value' member (no-member)


"""