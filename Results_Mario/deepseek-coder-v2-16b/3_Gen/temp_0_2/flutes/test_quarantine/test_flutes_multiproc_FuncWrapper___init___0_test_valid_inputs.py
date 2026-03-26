
import pytest
from flutes.multiproc import FuncWrapper

def test_valid_inputs():
    def add(a, b):
        return a + b
    
    wrapper = FuncWrapper(add, (1, 2), {'b': 3})
    result = wrapper.call()
    assert result == 4

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_FuncWrapper___init___0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___0_test_valid_inputs.py:10:13: E1101: Instance of 'FuncWrapper' has no 'call' member (no-member)


"""