
import pytest
from multiprocessing import Queue
from typing import Callable, Iterator, Optional, TypeVar
from flutes.multiproc import _gather_fn  # Assuming the module name is correct and the function is defined here

# Define type variables for clarity in tests
T = TypeVar('T')
R = TypeVar('R')

END_SIGNATURE = object()  # Define a sentinel value to simulate end of results

def test_gather_fn_with_simple_function():
    def add(a, b):
        return a + b
    
    q = Queue()
    _gather_fn(q, add, 3, b=4)
    results = []
    while not q.empty():
        result = q.get()
        if result != END_SIGNATURE:
            results.append(result)
    
    assert len(results) == 1
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

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0.py F             [100%]

=================================== FAILURES ===================================
_____________________ test_gather_fn_with_simple_function ______________________

    def test_gather_fn_with_simple_function():
        def add(a, b):
            return a + b
    
        q = Queue()
        _gather_fn(q, add, 3, b=4)
        results = []
        while not q.empty():
            result = q.get()
            if result != END_SIGNATURE:
                results.append(result)
    
>       assert len(results) == 1
E       assert 0 == 1
E        +  where 0 = len([])

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0.py:25: AssertionError
----------------------------- Captured stdout call -----------------------------
[2026-03-25 07:04:01] Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-25 07:04:01] <TypeError> 'int' object is not iterable
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

ERROR    flutes.log:log.py:182 <TypeError> 'int' object is not iterable
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0.py::test_gather_fn_with_simple_function
============================== 1 failed in 0.10s ===============================
"""