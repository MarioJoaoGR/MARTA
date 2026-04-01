
import pytest
from typing import List, Callable, Tuple, Any, Dict, TypeVar

R = TypeVar('R')

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

def test_edge_cases():
    # Test with None input
    with pytest.raises(TypeError):
        _chain_fns([lambda x: x], [None])
    
    # Test with empty lists
    assert _chain_fns([lambda x: x], []) == []
    
    # Test with boundary values
    def add(a, b):
        return a + b
    
    def multiply(a, b, c=1):
        return a * b * c
    
    fns = [add, multiply]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
    results = _chain_fns(fns, fn_arg_kwargs)
    assert results == [3, 60]
