
import pytest
from pymonet.utils import fn  # Assuming the module and function are correctly imported from 'pymonet.utils'

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case for invalid input (non-callable)
        curried_add = fn(5)  # Passing a non-callable object should raise TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_fn_0_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_utils_fn_0_test_invalid_inputs.py:3:0: E0611: No name 'fn' in module 'pymonet.utils' (no-name-in-module)


"""