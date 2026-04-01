
from pymonet.validation import Validation
import pytest

def test_success():
    val = Validation.success("Success")
    assert val.value == "Success"
    assert len(val.errors) == 0

def test_add_error():
    val = Validation.success()
    val.add_error("An error occurred")
    assert len(val.errors) == 1
    assert val.errors[0] == "An error occurred"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_success_1_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_success_1_test_edge_cases.py:12:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""