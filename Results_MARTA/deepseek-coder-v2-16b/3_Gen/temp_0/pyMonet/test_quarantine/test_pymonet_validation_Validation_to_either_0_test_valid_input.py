
import pytest
from pymonet.either import Left, Right
from your_module_path import Validation  # Replace 'your_module_path' with the actual path to your module

def test_valid_input():
    val = Validation("Success", [])
    assert val.value == "Success"
    assert len(val.errors) == 0
    either_val = val.to_either()
    assert isinstance(either_val, Right)
    assert either_val.value == "Success"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_either_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_valid_input.py:4:0: E0401: Unable to import 'your_module_path' (import-error)


"""