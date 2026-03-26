
# Importing necessary modules
import pytest
from pymonet.utils import fn  # Correctly importing the function from the specified module

def test_fn():
    def add(a, b):
        return a + b
    
    curried_add = fn(add)
    
    assert curried_add(1)(2) == 3  # Partially applying the function with one argument
    assert curried_add(1, 2) == 3   # Calling the function directly with both arguments

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_fn_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_utils_fn_0_test_edge_cases.py:4:0: E0611: No name 'fn' in module 'pymonet.utils' (no-name-in-module)


"""