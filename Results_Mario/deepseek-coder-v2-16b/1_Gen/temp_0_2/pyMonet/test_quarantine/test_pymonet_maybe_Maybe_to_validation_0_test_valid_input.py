
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    validation = maybe.to_validation()
    
    assert isinstance(validation, Validation)
    assert validation.is_success()
    assert validation.get_value() == 42

def test_empty_input():
    maybe = Maybe(value=None, is_nothing=True)
    validation = maybe.to_validation()
    
    assert isinstance(validation, Validation)
    assert validation.is_success()
    assert validation.get_value() is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_maybe_Maybe_to_validation_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_validation_0_test_valid_input.py:12:11: E1101: Instance of 'Validation' has no 'get_value' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_validation_0_test_valid_input.py:20:11: E1101: Instance of 'Validation' has no 'get_value' member (no-member)


"""