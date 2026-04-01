
from pymonet.validation import Validation
import pytest

def test_edge_cases():
    # Test with no errors
    val = Validation(10, [])
    lazy_val = val.to_lazy()
    assert lazy_val.fold() == 10

    # Test with errors
    val_with_error = Validation(None, ["Error message"])
    lazy_val_with_error = val_with_error.to_lazy()
    assert lazy_val_with_error.fold() is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_lazy_1_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_lazy_1_test_edge_cases.py:9:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_lazy_1_test_edge_cases.py:14:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""