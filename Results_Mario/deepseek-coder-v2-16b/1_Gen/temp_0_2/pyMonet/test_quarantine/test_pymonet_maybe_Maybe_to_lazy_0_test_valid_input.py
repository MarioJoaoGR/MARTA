
import pytest
from pymonet.maybe import Maybe
from pymonet.lazy import Lazy

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    lazy_maybe = maybe.to_lazy()
    result = lazy_maybe.fold()
    assert result == 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_maybe_Maybe_to_lazy_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_lazy_0_test_valid_input.py:9:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""