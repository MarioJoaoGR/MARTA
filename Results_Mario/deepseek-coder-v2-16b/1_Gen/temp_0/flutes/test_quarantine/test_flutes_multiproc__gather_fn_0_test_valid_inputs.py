
import pytest
from multiprocessing import Queue
from flutes.multiproc import _gather_fn, END_SIGNATURE
from typing import Callable, Iterator, Optional, TypeVar
from types import FunctionType

T = TypeVar('T')
R = TypeVar('R')

def example_fn(x: int) -> Iterator[int]:
    yield x * 2
    yield x * 3

def test_valid_inputs():
    q = Queue()
    result = _gather_fn(q, example_fn, 5)
    assert result is True
    
    items = []
    while not q.empty():
        items.append(q.get())
    
    # Remove the END_SIGNAL from the list before comparison
    if END_SIGNATURE in items:
        items.remove(END_SIGNATURE)
    
    assert items == [10, 15]

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

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        q = Queue()
        result = _gather_fn(q, example_fn, 5)
        assert result is True
    
        items = []
        while not q.empty():
            items.append(q.get())
    
        # Remove the END_SIGNAL from the list before comparison
        if END_SIGNATURE in items:
            items.remove(END_SIGNATURE)
    
>       assert items == [10, 15]
E       assert [] == [10, 15]
E         
E         Right contains 2 more items, first extra item: 10
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_valid_inputs.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""