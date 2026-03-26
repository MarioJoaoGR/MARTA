
import pytest
from queue import Queue
from pytutils.queues import multiplex
from threading import Thread

def test_valid_input():
    in_q = Queue()
    out_queues = multiplex(in_q, count=3)
    
    # Add an item to the input queue
    in_q.put("test")
    
    # Check that each output queue has received the item
    for q in out_queues:
        assert not q.empty()
        assert q.get() == "test"
        q.task_done()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        in_q = Queue()
        out_queues = multiplex(in_q, count=3)
    
        # Add an item to the input queue
        in_q.put("test")
    
        # Check that each output queue has received the item
        for q in out_queues:
>           assert not q.empty()
E           assert not True
E            +  where True = empty()
E            +    where empty = <queue.Queue object at 0x7f1fd3a3ba90>.empty

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_valid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""