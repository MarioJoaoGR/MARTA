
import pytest
from pymonet.validation import Validation

def test_error_handling():
    # Create a successful validation instance
    val = Validation.success("Success")
    
    # Attempt to call add_error method, which should not be present in the success instance
    with pytest.raises(AttributeError):
        val.add_error("An error occurred")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_success_2_test_error_handling
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_success_2_test_error_handling.py:11:8: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""