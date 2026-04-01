
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation("Success", [])
    assert val.value == "Success"
    assert len(val.errors) == 0
    
    val.add_error("An error occurred")
    assert len(val.errors) == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation___init___0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation___init___0_test_valid_inputs.py:10:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""