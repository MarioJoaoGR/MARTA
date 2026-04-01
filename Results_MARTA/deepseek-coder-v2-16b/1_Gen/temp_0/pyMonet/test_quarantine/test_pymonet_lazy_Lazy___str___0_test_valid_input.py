
from pymonet.lazy import Lazy
import pytest

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert str(lazy) == 'Lazy[fn=<function test_valid_input.<locals>.square at 0x...>, value=None, is_evaluated=False]'
    
    result = lazy.fold(5)
    assert str(lazy) == 'Lazy[fn=<function test_valid_input.<locals>.square at 0x...>, value=25, is_evaluated=True]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy___str___0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___str___0_test_valid_input.py:12:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""