
import pytest
from pymonet.utils import find

def memoized_fn(fn, key):
    cache = []
    
    def inner(argument):
        cached_result = find(cache, lambda cacheItem: key(cacheItem[0], argument))
        if cached_result is not None:
            return cached_result[1]
        fn_result = fn(argument)
        cache.append((argument, fn_result))
        return fn_result
    
    return inner

def test_invalid_input():
    with pytest.raises(TypeError):
        memoized_fn(lambda x: x * 2, lambda key, arg: arg)(None)
