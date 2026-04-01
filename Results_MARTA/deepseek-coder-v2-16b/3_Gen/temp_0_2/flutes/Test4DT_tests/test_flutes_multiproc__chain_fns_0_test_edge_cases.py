
import pytest
from typing import List, Callable, Tuple, Any, Dict, TypeVar

# Define type variables for clarity
R = TypeVar('R')

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

# Test case for _chain_fns function
def test_chain_fns():
    # Define example functions and their argument-keyword pairs
    def func1(a, b):
        return a + b
    
    def func2(x, y=0):
        return x * y
    
    fns = [func1, func2]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3,), {'y': 4} )]
    
    # Call the function and check the result
    result = _chain_fns(fns, fn_arg_kwargs)
    assert result == [3, 12]
