
import pytest
from typing import List, Callable, Tuple, Any, Dict

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

# Example functions to be tested
def func1(a, b):
    return a + b

def func2(x, y=0):
    return x * y

# Test cases for _chain_fns function
@pytest.mark.parametrize("fns, fn_arg_kwargs, expected", [
    (
        [func1, func2],
        [( (1, 2), {} ), ( (3,), {'y': 4} )],
        [3, 12]
    ),
    # Add more test cases as needed
])
def test_valid_inputs(fns, fn_arg_kwargs, expected):
    result = _chain_fns(fns, fn_arg_kwargs)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_1_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_1_test_valid_inputs.py:5:39: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_1_test_valid_inputs.py:5:113: E0602: Undefined variable 'R' (undefined-variable)


"""