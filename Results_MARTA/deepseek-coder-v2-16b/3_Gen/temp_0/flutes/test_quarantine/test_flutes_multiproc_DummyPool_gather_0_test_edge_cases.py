
import pytest
from flutes.multiproc import DummyPool

def test_dummy_pool_gather():
    dummy_pool = DummyPool(processes=0)
    
    def process_item(x):
        return x * 2
    
    items = [1, 2, 3, 4]
    results = list(dummy_pool.gather(process_item, items))
    
    assert results == [2, 4, 6, 8], "Results do not match expected values"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
____________________________ test_dummy_pool_gather ____________________________

    def test_dummy_pool_gather():
        dummy_pool = DummyPool(processes=0)
    
        def process_item(x):
            return x * 2
    
        items = [1, 2, 3, 4]
>       results = list(dummy_pool.gather(process_item, items))

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0_test_edge_cases.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.DummyPool object at 0x7f2bdcd80290>
fn = <function test_dummy_pool_gather.<locals>.process_item at 0x7f2bdcd8fd80>
iterable = [1, 2, 3, 4], args = (), kwds = {}, _ = (), __ = {}, x = 1

    def gather(self, fn: Callable[[T], Iterator[R]], iterable: Iterable[T], *_, args=(), kwds={}, **__) -> Iterator[R]:
        if self._process_state is not None:
            locals().update({"__state__": self._process_state})
        for x in iterable:
>           yield from fn(x, *args, **kwds)  # type: ignore[call-arg]
E           TypeError: 'int' object is not iterable

flutes/flutes/multiproc.py:114: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0_test_edge_cases.py::test_dummy_pool_gather
============================== 1 failed in 0.13s ===============================
"""