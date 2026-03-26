
import multiprocessing as mp
from flutes.multiproc import DummyPool
import pytest

@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0)

def test_dummy_pool_map_async(dummy_pool):
    def my_function(x):
        return x * 2
    
    iterable = [1, 2, 3, 4]
    result = dummy_pool.map_async(my_function, iterable)
    
    assert isinstance(result, mp.pool.ApplyResult)
    assert list(result.get()) == [2, 4, 6, 8]

def test_dummy_pool_map_async_with_args(dummy_pool):
    def my_function(x, factor=1):
        return x * factor
    
    iterable = [1, 2, 3, 4]
    args = (2,)
    result = dummy_pool.map_async(my_function, iterable, args=args)
    
    assert isinstance(result, mp.pool.ApplyResult)
    assert list(result.get()) == [2, 4, 6, 8]

def test_dummy_pool_map_async_with_kwds(dummy_pool):
    def my_function(x, factor=1):
        return x * factor
    
    iterable = [1, 2, 3, 4]
    kwds = {'factor': 2}
    result = dummy_pool.map_async(my_function, iterable, kwds=kwds)
    
    assert isinstance(result, mp.pool.ApplyResult)
    assert list(result.get()) == [2, 4, 6, 8]

def test_dummy_pool_map_async_with_args_and_kwds(dummy_pool):
    def my_function(x, factor=1):
        return x * factor
    
    iterable = [1, 2, 3, 4]
    args = (2,)
    kwds = {'factor': 2}
    result = dummy_pool.map_async(my_function, iterable, args=args, kwds=kwds)
    
    assert isinstance(result, mp.pool.ApplyResult)
    assert list(result.get()) == [4, 8, 12, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_edge_cases.py . [ 25%]
..F                                                                      [100%]

=================================== FAILURES ===================================
_________________ test_dummy_pool_map_async_with_args_and_kwds _________________

dummy_pool = <flutes.multiproc.DummyPool object at 0x7fdb6d2510d0>

    def test_dummy_pool_map_async_with_args_and_kwds(dummy_pool):
        def my_function(x, factor=1):
            return x * factor
    
        iterable = [1, 2, 3, 4]
        args = (2,)
        kwds = {'factor': 2}
>       result = dummy_pool.map_async(my_function, iterable, args=args, kwds=kwds)

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_edge_cases.py:49: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:90: in map_async
    return DummyApplyResult(self.map(fn, iterable, args=args, kwds=kwds))
flutes/flutes/multiproc.py:86: in map
    return list(self.imap(fn, iterable, args=args, kwds=kwds))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.DummyPool object at 0x7fdb6d2510d0>
fn = <function test_dummy_pool_map_async_with_args_and_kwds.<locals>.my_function at 0x7fdb6d25cb80>
iterable = [1, 2, 3, 4], args = (2,), kwds = {'factor': 2}, _ = (), __ = {}
x = 1

    def imap(self, fn: Callable[[T], R], iterable: Iterable[T], *_, args=(), kwds={}, **__) -> Iterator[R]:
        if self._process_state is not None:
            locals().update({"__state__": self._process_state})
        for x in iterable:
>           yield fn(x, *args, **kwds)  # type: ignore[call-arg]
E           TypeError: test_dummy_pool_map_async_with_args_and_kwds.<locals>.my_function() got multiple values for argument 'factor'

flutes/flutes/multiproc.py:80: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_edge_cases.py::test_dummy_pool_map_async_with_args_and_kwds
========================= 1 failed, 3 passed in 0.12s ==========================
"""