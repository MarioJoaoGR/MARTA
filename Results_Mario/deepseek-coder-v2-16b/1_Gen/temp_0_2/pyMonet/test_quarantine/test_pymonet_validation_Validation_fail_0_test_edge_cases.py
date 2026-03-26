
from pymonet.validation import Validation
import pytest

def test_fail():
    validation = Validation.fail(errors=["Error 1", "Error 2"])
    assert validation.has_errors() is True
    assert validation.get_value() is None
    assert validation.errors == ["Error 1", "Error 2"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_fail_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_fail_0_test_edge_cases.py:7:11: E1101: Instance of 'Validation' has no 'has_errors' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_fail_0_test_edge_cases.py:8:11: E1101: Instance of 'Validation' has no 'get_value' member (no-member)


"""