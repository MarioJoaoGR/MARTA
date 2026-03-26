
import pytest
from multiprocessing import Queue
from flutes.multiproc import _gather_fn, END_SIGNATURE
from typing import Callable, Iterator, Optional, TypeVar
from types import SimpleNamespace

T = TypeVar('T')
R = TypeVar('R')

def test_edge_cases():
    q = Queue()
    
    # Test with lambda that returns None
    result1 = _gather_fn(q, lambda: None)
    assert not q.empty(), "Queue should not be empty after function call"

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

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        q = Queue()
    
        # Test with lambda that returns None
        result1 = _gather_fn(q, lambda: None)
>       assert not q.empty(), "Queue should not be empty after function call"
E       AssertionError: Queue should not be empty after function call
E       assert not True
E        +  where True = empty()
E        +    where empty = <multiprocessing.queues.Queue object at 0x7f15c5f6a4d0>.empty

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_edge_cases.py:16: AssertionError
----------------------------- Captured stdout call -----------------------------
[2026-03-24 16:20:22] Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'NoneType' object is not iterable

[2026-03-24 16:20:22] <TypeError> 'NoneType' object is not iterable
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'NoneType' object is not iterable

ERROR    flutes.log:log.py:182 <TypeError> 'NoneType' object is not iterable
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""