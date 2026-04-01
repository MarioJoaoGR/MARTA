
import pytest
from typing import List, Callable, Tuple, Any, Dict

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

# Test case to check invalid inputs
def test_invalid_inputs():
    # Invalid fns input: not a list of callables
    with pytest.raises(TypeError):
        _chain_fns("not_a_list", [((), {})])
    
    # Invalid fn_arg_kwargs input: not a list of tuples
    with pytest.raises(TypeError):
        _chain_fns([lambda x, y: x + y], "not_a_tuple")
    
    # Invalid tuple in fn_arg_kwargs: args is not a tuple
    with pytest.raises(TypeError):
        _chain_fns([lambda x, y: x + y], [(123, {}), ((), {})])
    
    # Invalid tuple in fn_arg_kwargs: kwargs is not a dict
    with pytest.raises(TypeError):
        _chain_fns([lambda x, y: x + y], [((1, 2), 123)])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_invalid_inputs.py:5:39: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_invalid_inputs.py:5:113: E0602: Undefined variable 'R' (undefined-variable)

"""