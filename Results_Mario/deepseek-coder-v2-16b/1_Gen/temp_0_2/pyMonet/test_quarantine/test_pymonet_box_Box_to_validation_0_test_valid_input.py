
from pymonet.box import Box
from pymonet.validation import Validation
import pytest

def test_valid_input():
    box = Box(123)  # Create a Box instance with an integer value
    validation = box.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_success() is True
    assert validation.get_value() == 123

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_validation_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_validation_0_test_valid_input.py:11:11: E1101: Instance of 'Validation' has no 'get_value' member (no-member)


"""