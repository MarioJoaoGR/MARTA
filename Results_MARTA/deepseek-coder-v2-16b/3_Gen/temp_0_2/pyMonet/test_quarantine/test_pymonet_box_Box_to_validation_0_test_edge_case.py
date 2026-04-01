
import pytest
from pymonet.validation import Validation
from pymonet.box import Box

def test_edge_case():
    # Create a Box instance with an initial value
    box = Box(123)
    
    # Convert the Box to a Validation monad
    validation = box.to_validation()
    
    # Assert that the conversion was successful and the value is correct
    assert isinstance(validation, Validation)
    assert validation.is_success()
    assert validation.get_value() == 123

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_validation_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_validation_0_test_edge_case.py:16:11: E1101: Instance of 'Validation' has no 'get_value' member (no-member)


"""