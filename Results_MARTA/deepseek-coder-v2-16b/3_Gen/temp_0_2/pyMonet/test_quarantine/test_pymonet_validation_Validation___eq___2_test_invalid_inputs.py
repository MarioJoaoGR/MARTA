
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    val_error = Validation(None, ['Error message'])
    try:
        raise ValueError('Testing exception')
    except ValueError as e:
        val_exception = Validation(None, [str(e)])
    
    assert val_error.errors == ['Error message']
    assert val_exception.errors == ['Testing exception']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation___eq___2_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation___eq___2_test_invalid_inputs.py:13:11: E0601: Using variable 'val_exception' before assignment (used-before-assignment)


"""