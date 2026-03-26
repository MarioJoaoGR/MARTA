
import pytest
from typing import List, Callable, Tuple, Any, Dict

# Assuming _chain_fns is defined in a module named flutes.multiproc
# from flutes.multiproc import _chain_fns

def test_invalid_inputs():
    def add(a, b):
        return a + b
    
    def multiply(a, b, c=1):
        return a * b * c
    
    fns = [add, multiply]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
    # Test with invalid inputs: non-list fns and fn_arg_kwargs
    with pytest.raises(TypeError):
        _chain_fns("not a list", fn_arg_kwargs)
        
    with pytest.raises(TypeError):
        _chain_fns([add, multiply], "not a list")
        
    # Test with invalid inputs: incorrect types for fns and fn_arg_kwargs
    with pytest.raises(TypeError):
        _chain_fns("not a list", "not a list")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_2_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_invalid_inputs.py:20:8: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_invalid_inputs.py:23:8: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_invalid_inputs.py:27:8: E0602: Undefined variable '_chain_fns' (undefined-variable)


"""