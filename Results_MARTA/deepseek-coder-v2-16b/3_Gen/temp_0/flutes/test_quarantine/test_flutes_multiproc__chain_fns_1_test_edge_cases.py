
import pytest
from typing import List, Callable, Tuple, Any, Dict

# Assuming _chain_fns is defined in a module named flutes.multiproc
# from flutes.multiproc import _chain_fns

def test_edge_cases():
    def add(a, b):
        return a + b
    
    def multiply(a, b, c=1):
        return a * b * c
    
    fns = [add, multiply]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
    results = _chain_fns(fns, fn_arg_kwargs)
    assert results == [3, 60], "Expected results to be [3, 60]"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_1_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_1_test_edge_cases.py:18:14: E0602: Undefined variable '_chain_fns' (undefined-variable)


"""