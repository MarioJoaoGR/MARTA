
from typing import List, Callable, Tuple, Any, Dict, TypeVar
import pytest

R = TypeVar('R')

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

# Test case for _chain_fns function
def test_chain_fns():
    def add(a, b):
        return a + b
    
    def multiply(a, b, c=1):
        return a * b * c
    
    fns = [add, multiply]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
    results = _chain_fns(fns, fn_arg_kwargs)
    assert results == [3, 60], "Expected results to be [3, 60]"
