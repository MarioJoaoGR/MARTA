
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []
    
    # Applying a function to the validation instance
    def mapper(x):
        return x * 2
    
    new_val = val.apply_function(mapper)
    assert new_val is not None
    assert new_val.value == 20
    assert new_val.errors == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_success_0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_success_0_test_valid_inputs.py:14:14: E1101: Instance of 'Validation' has no 'apply_function' member (no-member)


"""