
import pytest
from typing import List, Callable, Any, Dict, Tuple, TypeVar

R = TypeVar('R')

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

# Test cases for edge cases
def test_edge_cases():
    # Test with empty lists
    assert _chain_fns([], []) == []
    
    # Test with None values in the input lists
    with pytest.raises(TypeError):
        _chain_fns(None, [((), {})])
    with pytest.raises(TypeError):
        _chain_fns([lambda x: x], None)
    
    # Test with functions that take different number of arguments
    def func1(a, b):
        return a + b
    
    def func2(x, y=0):
        return x * y
    
    fns = [func1, func2]
    fn_arg_kwargs = [((), {}), ((3,), {'y': 4})]
    
    # Test with correct input
    assert _chain_fns(fns, fn_arg_kwargs) == [3, 12]
    
    # Test with incorrect length of fns and fn_arg_kwargs
    with pytest.raises(IndexError):
        _chain_fns([func1], [((), {})])
    with pytest.raises(IndexError):
        _chain_fns([func1, func2], [((), {})])
    
    # Test with None values in the argument-keyword pairs
    fn_arg_kwargs = [((None,), {'y': 4}), ((3,), {'y': None})]
    with pytest.raises(TypeError):
        _chain_fns(fns, fn_arg_kwargs)
    
    # Test with empty argument-keyword pairs
    assert _chain_fns(fns, [(((), {})]) == [None]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_0_test_edge_cases.py:49:38: E0001: Parsing failed: 'closing parenthesis ']' does not match opening parenthesis '(' (Test4DT_tests.test_flutes_multiproc__chain_fns_0_test_edge_cases, line 49)' (syntax-error)


"""