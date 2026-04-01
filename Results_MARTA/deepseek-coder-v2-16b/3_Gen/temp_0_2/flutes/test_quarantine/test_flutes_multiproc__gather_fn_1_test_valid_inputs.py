
import multiprocessing as mp
from typing import Callable, Iterator, Optional, TypeVar, cast
from unittest.mock import Mock, patch
from flutes.multiproc import _gather_fn, END_SIGNATURE, log_exception

T = TypeVar('T')
R = TypeVar('R')

def test_valid_inputs():
    queue = mp.Queue()
    fn = Mock(spec=Callable[[T], Iterator[R]])
    args = (1,)
    kwargs = {'a': 'test'}

    with patch('flutes.multiproc.log_exception') as log_mock:
        result = _gather_fn(queue, fn, *args, **kwargs)

    assert result is True
    # Verify that the function was called correctly and the queue contains the expected items
    fn.assert_called_once_with(*args, **kwargs)
    
    for i in range(10):  # Assuming fn yields 10 items
        item = f"item_{i}"
        assert queue.get() == item

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

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        queue = mp.Queue()
        fn = Mock(spec=Callable[[T], Iterator[R]])
        args = (1,)
        kwargs = {'a': 'test'}
    
        with patch('flutes.multiproc.log_exception') as log_mock:
            result = _gather_fn(queue, fn, *args, **kwargs)
    
        assert result is True
        # Verify that the function was called correctly and the queue contains the expected items
        fn.assert_called_once_with(*args, **kwargs)
    
        for i in range(10):  # Assuming fn yields 10 items
            item = f"item_{i}"
>           assert queue.get() == item
E           AssertionError: assert (b'END',) == 'item_0'
E            +  where (b'END',) = get()
E            +    where get = <multiprocessing.queues.Queue object at 0x7fd8e5047890>.get

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_1_test_valid_inputs.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""