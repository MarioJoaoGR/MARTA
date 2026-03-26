
import pytest
from typing import List, Callable, Tuple, Dict, Any, Type

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

def test_invalid_inputs():
    # Test case 1: fns is None
    with pytest.raises(TypeError):
        _chain_fns(None, [((), {})])
    
    # Test case 2: fn_arg_kwargs is None
    with pytest.raises(TypeError):
        _chain_fns([lambda x: x], None)
    
    # Test case 3: fns and fn_arg_kwargs are empty lists
    assert _chain_fns([], []) == []
    
    # Test case 4: Length mismatch between fns and fn_arg_kwargs
    with pytest.raises(IndexError):
        _chain_fns([lambda x: x, lambda y: y], [((), {})])
    
    # Test case 5: Invalid argument types for fns and fn_arg_kwargs
    with pytest.raises(TypeError):
        _chain_fns("not a list", [{(): {}}])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_4_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_4_test_invalid_inputs.py:5:39: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_4_test_invalid_inputs.py:5:113: E0602: Undefined variable 'R' (undefined-variable)

"""