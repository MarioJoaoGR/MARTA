
import pytest
from typing import List, Callable, Tuple, Any, Dict, TypeVar

R = TypeVar('R')

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

def test_chain_fns_edge_cases():
    # Test with None input
    with pytest.raises(TypeError):
        _chain_fns(None, [])
    
    # Test with empty lists
    assert _chain_fns([], []) == []
    
    # Define some test functions and their argument-keyword pairs
    def func1(a, b):
        return a + b
    
    def func2(x, y=0):
        return x * y
    
    fns = [func1, func2]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3,), {'y': 4} )]
    
    # Test with valid input
    result = _chain_fns(fns, fn_arg_kwargs)
    assert result == [3, 12]
    
    # Test with invalid argument count
    with pytest.raises(TypeError):
        _chain_fns([func1], [((), {})])
    
    # Test with invalid keyword arguments
    with pytest.raises(TypeError):
        _chain_fns([func1], [((1, 2), {'a': 3})])
