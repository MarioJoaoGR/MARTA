
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    val = Validation(10, []).map(lambda x: raise ValueError('Test Error'))
    assert val.has_errors() == True
    assert val.get_value() is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_is_fail_1_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_fail_1_test_invalid_inputs.py:6:44: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_pymonet_validation_Validation_is_fail_1_test_invalid_inputs, line 6)' (syntax-error)


"""