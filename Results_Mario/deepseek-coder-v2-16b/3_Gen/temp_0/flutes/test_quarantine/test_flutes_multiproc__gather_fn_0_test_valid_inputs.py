
import pytest
from multiprocessing import Queue
from flutes.multiproc import _gather_fn, END_SIGNATURE
from typing import Callable, Iterator, Optional, TypeVar
from unittest.mock import patch

T = TypeVar('T')
R = TypeVar('R')

def example_fn(x):
    yield x * 2
    yield x * 3

@patch('flutes.multiproc._gather_fn')
def test_valid_inputs(_gather_fn_mock):
    q = Queue()
    _gather_fn_mock.return_value = True
    result = _gather_fn(q, example_fn, 5)
    assert result is True
    
    items = []
    while not q.empty():
        items.append(q.get())
    assert items == [10, 15]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

_gather_fn_mock = <MagicMock name='_gather_fn' id='139627037057680'>

    @patch('flutes.multiproc._gather_fn')
    def test_valid_inputs(_gather_fn_mock):
        q = Queue()
        _gather_fn_mock.return_value = True
        result = _gather_fn(q, example_fn, 5)
        assert result is True
    
        items = []
        while not q.empty():
            items.append(q.get())
>       assert items == [10, 15]
E       assert [10] == [10, 15]
E         
E         Right contains one more item: 15
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_valid_inputs.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.11s ===============================
"""