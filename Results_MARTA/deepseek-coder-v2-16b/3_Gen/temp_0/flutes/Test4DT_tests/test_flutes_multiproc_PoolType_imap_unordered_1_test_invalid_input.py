
import pytest
from multiprocessing import Pool
from functools import partial
from typing import Callable, Iterable, Iterator, Any, Mapping, List

# Assuming the module 'flutes.multiproc' has a class PoolType with an imap_unordered method
class PoolType:
    def imap_unordered(self, fn: Callable[[Any], Any], iterable: Iterable[Any], chunksize: int = 1, *, args: Iterable[Any] = (), kwds: Mapping[str, Any] = {}) -> Iterator[Any]:
        pass

def test_invalid_input():
    pool = PoolType()
    
    # Test with invalid input types
    with pytest.raises(TypeError):
        list(pool.imap_unordered("not a function", range(5)))  # fn is not callable
        
    with pytest.raises(TypeError):
        list(pool.imap_unordered(lambda x: x, "not an iterable"))  # iterable is not iterable
    
    with pytest.raises(TypeError):
        list(pool.imap_unordered(lambda x: x, range(5), chunksize="not an int"))  # chunksize is not an integer
        
    with pytest.raises(TypeError):
        list(pool.imap_unordered(lambda x: x, range(5), chunksize=1, args="not a tuple"))  # args is not a tuple
        
    with pytest.raises(TypeError):
        list(pool.imap_unordered(lambda x: x, range(5), chunksize=1, kwds="not a dictionary"))  # kwds is not a dictionary
