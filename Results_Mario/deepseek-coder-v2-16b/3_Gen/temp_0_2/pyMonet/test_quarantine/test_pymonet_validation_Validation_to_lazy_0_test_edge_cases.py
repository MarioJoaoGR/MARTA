
from pymonet.validation import Validation
from pymonet.lazy import Lazy
import pytest

def test_to_lazy():
    # Test when there are no errors
    val = Validation(10, [])
    lazy_val = val.to_lazy()
    assert lazy_val.fold() == 10

    # Test when there are errors
    val_with_error = Validation(None, ["Error message"])
    lazy_val_with_error = val_with_error.to_lazy()
    with pytest.raises(Exception):
        lazy_val_with_error.fold()  # This should raise an exception because there's an error

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_lazy_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_lazy_0_test_edge_cases.py:10:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_lazy_0_test_edge_cases.py:16:8: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""