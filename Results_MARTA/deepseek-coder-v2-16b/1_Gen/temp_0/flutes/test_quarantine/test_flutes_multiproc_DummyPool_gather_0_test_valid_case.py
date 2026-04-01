
import pytest
from flutes.multiproc import DummyPool

def test_valid_case():
    # Create a DummyPool instance with processes set to 0, which means single-threaded execution
    pool = DummyPool(processes=0)
    
    # Define a function to be processed by the pool
    def process_item(x):
        return x * 2
    
    # Create an iterable for processing
    data = [1, 2, 3, 4]
    
    # Use the pool to gather results from the process_item function applied to each item in the data
    results = list(pool.gather(process_item, data))
    
    # Assert that the results are as expected
    assert results == [2, 4, 6, 8]

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

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        # Create a DummyPool instance with processes set to 0, which means single-threaded execution
        pool = DummyPool(processes=0)
    
        # Define a function to be processed by the pool
        def process_item(x):
            return x * 2
    
        # Create an iterable for processing
        data = [1, 2, 3, 4]
    
        # Use the pool to gather results from the process_item function applied to each item in the data
>       results = list(pool.gather(process_item, data))

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0_test_valid_case.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.DummyPool object at 0x7fd0417d2c50>
fn = <function test_valid_case.<locals>.process_item at 0x7fd04192ac00>
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
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.10s ===============================
"""