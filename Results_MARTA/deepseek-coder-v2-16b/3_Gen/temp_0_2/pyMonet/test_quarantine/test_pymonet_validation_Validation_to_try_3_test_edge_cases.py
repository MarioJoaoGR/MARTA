
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test when there are no errors
    val = Validation(10, [])
    try_obj = val.to_try()
    assert try_obj.is_success(), "Expected success Try monad"
    
    # Test when there are errors
    val_with_errors = Validation("invalid", ["Error 1", "Error 2"])
    try_obj_with_errors = val_with_errors.to_try()
    assert not try_obj_with_errors.is_success(), "Expected failed Try monad"
    assert try_obj_with_errors.get_error_messages() == ["Error 1", "Error 2"], "Expected specific error messages in the Try monad"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_try_3_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_try_3_test_edge_cases.py:15:11: E1101: Instance of 'Try' has no 'get_error_messages' member (no-member)


"""