
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation(10, [])
    assert val.value == 10
    assert not val.errors
    
    # Applying a function that should succeed
    def add_one(x):
        return x + 1
    
    new_val = val.apply_function(add_one)
    assert new_val is not None
    assert new_val.value == 11
    assert not new_val.errors

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation___str___0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation___str___0_test_valid_inputs.py:14:14: E1101: Instance of 'Validation' has no 'apply_function' member (no-member)


"""