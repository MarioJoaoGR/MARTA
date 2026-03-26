
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []
    
    # Applying a function that does nothing but returns the same value should not change the value or add errors
    def identity_function(x):
        return x
    
    new_val = val.apply_function(identity_function)
    assert isinstance(new_val, Validation)
    assert new_val.value == 10
    assert new_val.errors == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation___eq___0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation___eq___0_test_valid_inputs.py:14:14: E1101: Instance of 'Validation' has no 'apply_function' member (no-member)


"""