
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

def test_invalid_input():
    left_instance = Left("Error message")
    validation = left_instance.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_failure()
    assert validation.errors == ["Error message"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_to_validation_0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_either_Left_to_validation_0_test_invalid_input.py:10:11: E1101: Instance of 'Validation' has no 'is_failure' member (no-member)


"""