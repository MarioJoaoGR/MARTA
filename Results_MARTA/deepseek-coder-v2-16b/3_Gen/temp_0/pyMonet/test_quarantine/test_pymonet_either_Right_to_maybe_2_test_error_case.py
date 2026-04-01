
import pytest
from pymonet.either import Right
from pymonet.maybe import Maybe

def test_right_to_maybe():
    # Test with a value
    right = Right(value=42)
    maybe = right.to_maybe()
    assert not maybe.is_nothing
    assert maybe.get_value() == 42

    # Test without a value (should return Nothing)
    error_right = Right()
    maybe_error = error_right.to_maybe()
    assert maybe_error.is_nothing

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_to_maybe_2_test_error_case
pyMonet/Test4DT_tests/test_pymonet_either_Right_to_maybe_2_test_error_case.py:11:11: E1101: Instance of 'Maybe' has no 'get_value' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_either_Right_to_maybe_2_test_error_case.py:14:18: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""