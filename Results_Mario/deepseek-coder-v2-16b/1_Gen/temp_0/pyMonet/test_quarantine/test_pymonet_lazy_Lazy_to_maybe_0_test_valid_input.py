
import pytest
from pymonet.lazy import Lazy
from pymonet.maybe import Maybe

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    maybe_lazy = lazy.to_maybe(5)
    
    assert isinstance(maybe_lazy, Maybe)
    assert maybe_lazy.is_just()
    assert maybe_lazy.get_value() == 25

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_to_maybe_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_maybe_0_test_valid_input.py:14:11: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_maybe_0_test_valid_input.py:15:11: E1101: Instance of 'Maybe' has no 'get_value' member (no-member)


"""