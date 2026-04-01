
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_inputs():
    def square(x):
        return x ** 2
    
    numbers = [1, 2, 3, 4]
    pool = DummyPool(processes=0)
    result_iter = pool.imap_unordered(square, numbers, args=((),), kwds={})
    
    results = list(result_iter)
    assert len(results) == len(numbers)
    for num in numbers:
        assert any(num ** 2 == r for r in results)

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

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        def square(x):
            return x ** 2
    
        numbers = [1, 2, 3, 4]
        pool = DummyPool(processes=0)
        result_iter = pool.imap_unordered(square, numbers, args=((),), kwds={})
    
>       results = list(result_iter)

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_0_test_valid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.DummyPool object at 0x7f06df8f4050>
fn = <function test_valid_inputs.<locals>.square at 0x7f06df855760>
iterable = [1, 2, 3, 4], args = ((),), kwds = {}, _ = (), __ = {}, x = 1

    def imap(self, fn: Callable[[T], R], iterable: Iterable[T], *_, args=(), kwds={}, **__) -> Iterator[R]:
        if self._process_state is not None:
            locals().update({"__state__": self._process_state})
        for x in iterable:
>           yield fn(x, *args, **kwds)  # type: ignore[call-arg]
E           TypeError: test_valid_inputs.<locals>.square() takes 1 positional argument but 2 were given

flutes/flutes/multiproc.py:80: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""