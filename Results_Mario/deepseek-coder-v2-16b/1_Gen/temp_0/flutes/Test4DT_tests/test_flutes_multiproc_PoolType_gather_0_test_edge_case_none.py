
import pytest
from multiprocessing import Pool
from typing import Iterator, Callable, Iterable, Any, Mapping

# Assuming PoolType and its methods are defined in a module named 'flutes.multiproc'
from flutes.multiproc import PoolType

def test_edge_case_none():
    pool = PoolType()
    
    # Test when fn is None
    with pytest.raises(TypeError):
        list(pool.gather(None, [1, 2, 3]))
    
    # Test when iterable is None
    def example_fn(x):
        yield x * 2
        yield x * 3
    
    with pytest.raises(TypeError):
        list(pool.gather(example_fn, None))
    
    # Test when both fn and iterable are None
    with pytest.raises(TypeError):
        list(pool.gather(None, None))
