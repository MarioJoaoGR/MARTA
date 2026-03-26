
import pytest
from typing import List, Callable, Tuple, Any, Dict

# Assuming _chain_fns is defined in a module named multiproc
# from flutes.multiproc import _chain_fns

def test_valid_inputs():
    def func1(a, b):
        return a + b
    
    def func2(x, y=0):
        return x * y
    
    fns = [func1, func2]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3,), {'y': 4} )]
    
    result = _chain_fns(fns, fn_arg_kwargs)
    
    assert result == [3, 12]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_valid_inputs.py:18:13: E0602: Undefined variable '_chain_fns' (undefined-variable)


"""