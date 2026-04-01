
import pytest
from pymonet.either import Left, Right
from your_module_name.validation import Validation

def test_valid_input():
    val = Validation("Success", [])
    assert val.is_success() is True
    either_val = val.to_either()
    assert isinstance(either_val, Right)
    assert either_val.value == "Success"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_either_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_valid_input.py:4:0: E0401: Unable to import 'your_module_name.validation' (import-error)


"""