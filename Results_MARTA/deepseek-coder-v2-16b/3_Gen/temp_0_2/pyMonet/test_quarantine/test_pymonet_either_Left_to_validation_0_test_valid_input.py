
import pytest
from pymonet.either import Left
from pymonet.validation import Validation

def test_valid_input():
    left_instance = Left(value="error")
    validation_result = left_instance.to_validation()
    
    assert isinstance(validation_result, Validation)
    assert validation_result.is_fail()
    assert validation_result.get_errors() == ["error"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_to_validation_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Left_to_validation_0_test_valid_input.py:12:11: E1101: Instance of 'Validation' has no 'get_errors' member (no-member)


"""