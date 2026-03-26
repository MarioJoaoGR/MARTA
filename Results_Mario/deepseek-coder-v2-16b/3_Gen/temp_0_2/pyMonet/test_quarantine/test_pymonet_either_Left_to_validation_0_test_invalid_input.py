
import pytest
from pymonet.either import Left
from pymonet.validation import Validation

def test_invalid_input():
    # Arrange
    left = Left(value="error message")
    
    # Act
    validation = left.to_validation()
    
    # Assert
    assert isinstance(validation, Validation)
    assert validation.is_fail()
    assert validation.get_errors() == ["error message"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_to_validation_0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_either_Left_to_validation_0_test_invalid_input.py:16:11: E1101: Instance of 'Validation' has no 'get_errors' member (no-member)


"""