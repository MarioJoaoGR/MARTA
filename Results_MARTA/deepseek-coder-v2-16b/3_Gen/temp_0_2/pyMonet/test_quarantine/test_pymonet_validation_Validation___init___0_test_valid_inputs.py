
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    # Test with valid inputs
    val = Validation(10, [])
    result = val.apply_function(lambda x: x * 2)
    assert result.value == 20
    assert result.errors == []

    # Test with invalid inputs (should have errors)
    val = Validation(10, ["Error1", "Error2"])
    result = val.apply_function(lambda x: x * 2)
    assert result is None
    assert val.errors == ["Error1", "Error2"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation___init___0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation___init___0_test_valid_inputs.py:8:13: E1101: Instance of 'Validation' has no 'apply_function' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation___init___0_test_valid_inputs.py:14:13: E1101: Instance of 'Validation' has no 'apply_function' member (no-member)


"""