
import pytest
from unittest.mock import MagicMock
from pytutils.queues import Queue

def test_valid_inputs():
    # Create mock queues
    q = Queue()
    out_queues = [Queue(), Queue()]
    
    # Mock the behavior of the queue and output queues
    items = ['item1', 'item2']
    for item in items:
        q.get = MagicMock(return_value=item)
        for out_q in out_queues:
            out_q.put = MagicMock()
    
    # Call the function with mocked queues
    f(q, out_queues)
    
    # Check if put was called on each output queue with the correct item
    assert q.get.call_count == len(items)
    for i, out_q in enumerate(out_queues):
        assert out_q.put.call_count == len(items)
        assert out_q.put.call_args_list[i] == [(item, ) for item in items]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_queues_f_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_queues_f_0_test_valid_inputs.py:19:4: E0602: Undefined variable 'f' (undefined-variable)


"""