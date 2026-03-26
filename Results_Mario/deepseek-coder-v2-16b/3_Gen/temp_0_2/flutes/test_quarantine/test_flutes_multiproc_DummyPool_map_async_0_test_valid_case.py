
import pytest
from flutes.multiproc import DummyPool

def test_valid_case():
    pool = DummyPool(processes=0)  # Create a single-threaded pool
    
    def initializer_func(state):
        global __state__
        __state__ = state
    
    # Apply a function to an iterable with the initializer set up
    results = list(pool.map_async(lambda x: x * 2, [1, 2, 3], args=(42,)))
    
    assert results == [84, 168, 252]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        pool = DummyPool(processes=0)  # Create a single-threaded pool
    
        def initializer_func(state):
            global __state__
            __state__ = state
    
        # Apply a function to an iterable with the initializer set up
>       results = list(pool.map_async(lambda x: x * 2, [1, 2, 3], args=(42,)))

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_valid_case.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:90: in map_async
    return DummyApplyResult(self.map(fn, iterable, args=args, kwds=kwds))
flutes/flutes/multiproc.py:86: in map
    return list(self.imap(fn, iterable, args=args, kwds=kwds))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.DummyPool object at 0x7fd23ae4fa10>
fn = <function test_valid_case.<locals>.<lambda> at 0x7fd23afede40>
iterable = [1, 2, 3], args = (42,), kwds = {}, _ = (), __ = {}, x = 1

    def imap(self, fn: Callable[[T], R], iterable: Iterable[T], *_, args=(), kwds={}, **__) -> Iterator[R]:
        if self._process_state is not None:
            locals().update({"__state__": self._process_state})
        for x in iterable:
>           yield fn(x, *args, **kwds)  # type: ignore[call-arg]
E           TypeError: test_valid_case.<locals>.<lambda>() takes 1 positional argument but 2 were given

flutes/flutes/multiproc.py:80: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.12s ===============================
"""