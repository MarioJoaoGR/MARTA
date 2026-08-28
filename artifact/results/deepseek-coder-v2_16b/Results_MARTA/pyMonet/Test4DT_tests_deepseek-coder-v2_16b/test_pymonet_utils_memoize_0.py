
import pytest
from typing import Callable, Any, List
from functools import partial
from operator import eq

# Assuming memoize function implementation is provided as described in the prompt.
def memoize(fn: Callable, key=eq) -> Callable:
    cache: List[Any] = []

    def memoized_fn(argument):
        cached_result = next((item for item in cache if key(item[0], argument)), None)
        if cached_result is not None:
            return cached_result[1]
        fn_result = fn(argument)
        cache.append((argument, fn_result))
        return fn_result

    return memoized_fn

# Test scenarios
def test_valid_input():
    def add(x):
        return x + 10
    
    memoized_add = memoize(add)
    assert memoized_add(5) == 15
    # The second call should retrieve from cache, so it should also be 15.
    assert memoized_add(5) == 15

def test_edge_case_none():
    def add(x):
        return x + 10
    
    memoized_add = memoize(add)
    with pytest.raises(TypeError):
        # None is not a valid input for the function, should raise an error
        assert memoized_add(None)

def test_invalid_input():
    def add(x):
        return x + 10
    
    memoized_add = memoize(add)
    with pytest.raises(TypeError):
        # 'invalid' is not a valid input for the function, should raise an error
        assert memoized_add('invalid')
