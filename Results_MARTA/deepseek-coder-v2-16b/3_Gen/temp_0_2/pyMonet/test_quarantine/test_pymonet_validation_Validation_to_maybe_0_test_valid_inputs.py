
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_valid_inputs():
    # Test with valid input and no errors
    val = Validation(10, [])
    maybe_val = val.to_maybe()
    assert isinstance(maybe_val, Maybe)
    assert maybe_val.is_just()
    assert maybe_val.get_value() == 10

    # Test with valid input but errors present (should return empty Maybe)
    val_with_errors = Validation(20, ["Error1", "Error2"])
    maybe_val_with_errors = val_with_errors.to_maybe()
    assert isinstance(maybe_val_with_errors, Maybe)
    assert not maybe_val_with_errors.is_just()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs.py:11:11: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs.py:12:11: E1101: Instance of 'Maybe' has no 'get_value' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs.py:18:15: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)


"""