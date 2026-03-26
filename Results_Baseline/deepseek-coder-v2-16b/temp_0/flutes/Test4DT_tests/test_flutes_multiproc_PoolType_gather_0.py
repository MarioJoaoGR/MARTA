# Module: flutes.multiproc
import pytest
from multiprocessing import Pool as MPPool
from typing import Callable, Iterable, Iterator, Any, Mapping

# Assuming PoolType is defined somewhere in flutes.multiproc module
# from flutes.multiproc import PoolType

def test_gather_basic():
    class PoolType:
        def gather(self, fn, iterable, chunksize=1, args=(), kwds={}):
            results = []
            for item in iterable:
                result = list(fn(item, *args, **kwds))
                results.extend(result)
            return iter(results)
    
    pool = PoolType()
    
    def example_fn(x):
        yield x * 2
        yield x * 3
    
    iterable = [1, 2, 3]
    results = list(pool.gather(example_fn, iterable))
    assert results == [2, 3, 4, 6, 6, 9], "Test failed: Incorrect results"

def test_gather_empty_iterable():
    class PoolType:
        def gather(self, fn, iterable, chunksize=1, args=(), kwds={}):
            return iter([])
    
    pool = PoolType()
    
    def example_fn(x):
        yield x * 2
        yield x * 3
    
    iterable = []
    results = list(pool.gather(example_fn, iterable))
    assert len(results) == 0, "Test failed: Non-empty result for empty iterable"

def test_gather_with_args():
    class PoolType:
        def gather(self, fn, iterable, chunksize=1, args=(), kwds={}):
            results = []
            for item in iterable:
                result = list(fn(item, *args, **kwds))
                results.extend(result)
            return iter(results)
    
    pool = PoolType()
    
    def example_fn(x, multiplier):
        yield x * multiplier
    
    iterable = [1, 2, 3]
    args = (2,)
    results = list(pool.gather(example_fn, iterable, args=args))
    assert results == [2, 4, 6], "Test failed: Incorrect results with arguments"

def test_gather_with_kwds():
    class PoolType:
        def gather(self, fn, iterable, chunksize=1, args=(), kwds={}):
            results = []
            for item in iterable:
                result = list(fn(item, *args, **kwds))
                results.extend(result)
            return iter(results)
    
    pool = PoolType()
    
    def example_fn(x, multiplier):
        yield x * multiplier
    
    iterable = [1, 2, 3]
    kwds = {'multiplier': 2}
    results = list(pool.gather(example_fn, iterable, kwds=kwds))
    assert results == [2, 4, 6], "Test failed: Incorrect results with keyword arguments"

def test_gather_large_chunksize():
    class PoolType:
        def gather(self, fn, iterable, chunksize=1, args=(), kwds={}):
            results = []
            for item in iterable:
                result = list(fn(item, *args, **kwds))
                results.extend(result)
            return iter(results)
    
    pool = PoolType()
    
    def example_fn(x):
        yield x * 2
        yield x * 3
    
    iterable = [1, 2, 3]
    chunksize = 2
    results = list(pool.gather(example_fn, iterable, chunksize=chunksize))
    assert results == [2, 3, 4, 6, 6, 9], "Test failed: Incorrect results with large chunksize"
