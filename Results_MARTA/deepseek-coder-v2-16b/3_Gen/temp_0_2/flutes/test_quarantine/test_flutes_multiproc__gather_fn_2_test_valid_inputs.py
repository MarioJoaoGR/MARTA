
import pytest
from multiprocessing import Queue
from typing import Iterator, Callable, Optional, TypeVar
from flutes.multiproc import _gather_fn, END_SIGNATURE

# Define type variables
T = TypeVar('T')
R = TypeVar('R')

def generate_items(num):
    yield from range(num)

def test_valid_inputs():
    q = Queue()
    fn = lambda x: (item for item in x)
    _gather_fn(q, fn, list(range(5)))
    
    results = []
    while not q.empty():
        results.append(q.get())
    
    assert len(results) == 6  # Should have 6 items: 5 from the range and 1 END_SIGNATURE
    for i in range(5):
        assert results[i] == i
    assert results[-1] is END_SIGNATURE

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

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        q = Queue()
        fn = lambda x: (item for item in x)
        _gather_fn(q, fn, list(range(5)))
    
        results = []
        while not q.empty():
            results.append(q.get())
    
>       assert len(results) == 6  # Should have 6 items: 5 from the range and 1 END_SIGNATURE
E       assert 1 == 6
E        +  where 1 = len([0])

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_2_test_valid_inputs.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.11s ===============================
"""