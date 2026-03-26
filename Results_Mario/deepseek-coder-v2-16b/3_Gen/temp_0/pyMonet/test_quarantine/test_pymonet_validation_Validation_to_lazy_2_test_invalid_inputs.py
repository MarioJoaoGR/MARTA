
import pytest
from pymonet.validation import Validation

def test_add_error():
    val = Validation("Success", [])
    assert len(val.errors) == 0
    
    val.add_error("An error occurred")
    assert len(val.errors) == 1
    assert val.errors[0] == "An error occurred"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_lazy_2_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_lazy_2_test_invalid_inputs.py:9:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""