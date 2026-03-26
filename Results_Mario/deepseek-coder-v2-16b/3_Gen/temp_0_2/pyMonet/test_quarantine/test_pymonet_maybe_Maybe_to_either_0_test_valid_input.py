
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    either = maybe_some.to_either()
    assert isinstance(either, Right)
    assert either.value == 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_maybe_Maybe_to_either_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_either_0_test_valid_input.py:8:30: E0602: Undefined variable 'Right' (undefined-variable)


"""