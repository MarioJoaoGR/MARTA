
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterable, Iterator, Any, Mapping

def test_imap():
    class MockPoolType(PoolType):
        def imap(self, fn, iterable, chunksize=1, args=(), kwds={}):
            results = []
            for item in iterable:
                result = fn(item, *args, **kwds)
                results.append(result)
            return iter(results)
    
    pool = MockPoolType()
    def square(x):
        return x ** 2
    
    iterable = [1, 2, 3, 4]
    results = pool.imap(square, iterable)
    assert list(results) == [1, 4, 9, 16]
