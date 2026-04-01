
import pytest
from pymonet.validation import Validation
from pymonet.maybe import Maybe

def test_to_maybe():
    # Test when there are no errors
    val = Validation(10, [])
    maybe_val = val.to_maybe()
    assert isinstance(maybe_val, Maybe)
    assert maybe_val.is_just()
    assert maybe_val.get_value() == 10

    # Test when there are errors
    val_with_errors = Validation("invalid", ["Error"])
    maybe_val_with_errors = val_with_errors.to_maybe()
    assert isinstance(maybe_val_with_errors, Maybe)
    assert not maybe_val_with_errors.is_just()
    assert maybe_val_with_errors.get_value() is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_maybe_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_edge_cases.py:11:11: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_edge_cases.py:12:11: E1101: Instance of 'Maybe' has no 'get_value' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_edge_cases.py:18:15: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_edge_cases.py:19:11: E1101: Instance of 'Maybe' has no 'get_value' member (no-member)


"""