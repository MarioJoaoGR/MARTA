
import pytest
from typing import List, Callable, Tuple, Any, Dict

# Assuming _chain_fns is defined in a module named flutes.multiproc
# from flutes.multiproc import _chain_fns

def test_invalid_inputs():
    # Define some sample functions and argument-keyword pairs
    def func1(a, b):
        return a + b
    
    def func2(x, y=0):
        return x * y
    
    fns = [func1, func2]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3,), {'y': 4} )]
    
    # Test with invalid inputs: passing None instead of list for fns
    with pytest.raises(TypeError):
        _chain_fns(None, fn_arg_kwargs)
    
    # Test with invalid inputs: passing None instead of list for fn_arg_kwargs
    with pytest.raises(TypeError):
        _chain_fns(fns, None)
    
    # Test with invalid inputs: passing empty lists
    assert _chain_fns([], []) == []
    
    # Test with invalid inputs: fns and fn_arg_kwargs have different lengths
    with pytest.raises(IndexError):
        _chain_fns(fns[:1], fn_arg_kwargs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_1_test_invalid_inputs.py:21:8: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_1_test_invalid_inputs.py:25:8: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_1_test_invalid_inputs.py:28:11: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_1_test_invalid_inputs.py:32:8: E0602: Undefined variable '_chain_fns' (undefined-variable)


"""