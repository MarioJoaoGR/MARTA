
import pytest
from typing import List, Callable, Tuple, Any, Dict

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

def test_valid_inputs():
    # Define a list of functions and their arguments
    fns = [lambda x, y: x + y, lambda x, y=2: x * y]
    fn_arg_kwargs = [((), {}), ((1,), {'y': 3})]
    
    # Call the function with the defined inputs
    results = _chain_fns(fns, fn_arg_kwargs)
    
    # Assert the expected output
    assert results == [None, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_valid_inputs.py:5:39: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_valid_inputs.py:5:113: E0602: Undefined variable 'R' (undefined-variable)


"""