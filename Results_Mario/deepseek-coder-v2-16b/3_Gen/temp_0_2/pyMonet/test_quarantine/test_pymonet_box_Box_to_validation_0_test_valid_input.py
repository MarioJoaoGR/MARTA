
import pytest
from pymonet.validation import Validation
from pymonet.box import Box

def test_valid_input():
    # Create a Box instance with valid input
    box = Box(123)
    
    # Convert the Box to a Validation instance
    validation = box.to_validation()
    
    # Assert that the conversion was successful and the value is correct
    assert isinstance(validation, Validation)
    assert validation.is_success()
    assert validation.get_value() == 123

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_validation_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_validation_0_test_valid_input.py:16:11: E1101: Instance of 'Validation' has no 'get_value' member (no-member)


"""