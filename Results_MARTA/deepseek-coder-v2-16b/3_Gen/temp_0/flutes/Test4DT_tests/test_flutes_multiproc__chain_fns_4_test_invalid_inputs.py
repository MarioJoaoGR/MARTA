
from typing import List, Callable, Tuple, Any, Dict
import pytest
from flutes.multiproc import _chain_fns

def add(a, b):
    return a + b

def multiply(a, b, c=1):
    return a * b * c

@pytest.mark.parametrize("fns, fn_arg_kwargs, expected", [
    ([add, multiply], [( (1, 2), {} ), ( (3, 4), {'c': 5} )], [3, 60]),
    # Add more test cases as needed
])
def test_invalid_inputs(fns, fn_arg_kwargs, expected):
    results = _chain_fns(fns, fn_arg_kwargs)
    assert results == expected
