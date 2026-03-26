
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    val = Validation('Success', ['Error1'])
    val.add_error('Error2')
    
    assert not val.is_success(), "Expected validation to fail with added errors"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_is_success_0_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_success_0_test_invalid_inputs.py:7:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""