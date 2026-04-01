
import pytest
from flutes.multiproc import _chain_fns
from typing import List, Callable, Tuple, Any, Dict, Type

def test_edge_cases():
    def add(a, b):
        return a + b
    
    def multiply(a, b, c=1):
        return a * b * c
    
    fns = [add, multiply]
    fn_arg_kwargs = [( (1, 2), {} ), ( (3, 4), {'c': 5} )]
    
    results = _chain_fns(fns, fn_arg_kwargs)
    assert results == [3, 60], "Expected results to be [3, 60]"
