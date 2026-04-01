
from pymonet.validation import Validation
import pytest

def test_invalid_inputs():
    # Test initialization with invalid inputs
    val = Validation("Success", [])  # This should pass since "Success" is not an error
    assert len(val.errors) == 0, "Expected no errors but got some."
    
    # Adding an error to the Validation instance
    val.add_error("An error occurred")
    assert len(val.errors) == 1, "Expected one error but got more or none."
    
    # Test adding non-string values to errors (should be ignored as per class definition)
    with pytest.raises(TypeError):
        val.add_error(None)  # This should raise a TypeError since None is not a string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_box_2_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_box_2_test_invalid_inputs.py:11:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_box_2_test_invalid_inputs.py:16:8: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""