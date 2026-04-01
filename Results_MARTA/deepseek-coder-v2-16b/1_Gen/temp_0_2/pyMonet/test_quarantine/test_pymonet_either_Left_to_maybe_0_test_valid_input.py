
import pytest
from pymonet.either import Left
from pymonet.maybe import Maybe

def test_valid_input():
    left = Left()
    maybe_left = left.to_maybe()
    assert isinstance(maybe_left, Maybe)
    assert maybe_left.is_nothing()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_to_maybe_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Left_to_maybe_0_test_valid_input.py:7:11: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""