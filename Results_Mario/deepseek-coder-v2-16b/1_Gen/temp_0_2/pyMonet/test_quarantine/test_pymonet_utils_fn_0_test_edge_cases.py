
import pytest
from pymonet.utils import fn  # Assuming 'fn' is defined in this module

def test_edge_cases():
    def add(a, b):
        return a + b
    
    curried_add = fn(add)
    assert curried_add(1)(2) == 3
    
    curried_add_three = fn(add, args_count=3)
    assert curried_add_three(1)(2)(3) == 6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_fn_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_utils_fn_0_test_edge_cases.py:3:0: E0611: No name 'fn' in module 'pymonet.utils' (no-name-in-module)


"""