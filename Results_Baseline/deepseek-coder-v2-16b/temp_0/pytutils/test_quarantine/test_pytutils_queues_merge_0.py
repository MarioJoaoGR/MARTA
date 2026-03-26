
import pytest
from queue import Queue, Empty  # Importing both Queue and Empty from the queue module
from threading import Thread
from pytutils.queues import merge

# Helper function to push elements from one queue to another for testing purposes
def push(src, dest):
    while True:
        try:
            item = src.get_nowait()
            dest.put_nowait(item)
        except Empty:
            break

@pytest.fixture
def setup_queues():
    q1 = Queue()
    q2 = Queue()
    q3 = Queue()
    return q1, q2, q3

def test_merge_with_three_queues(setup_queues):
    q1, q2, q3 = setup_queues
    out_q = merge(q1, q2, q3)
    
    # Add elements to the queues
    q1.put(1)
    q2.put(2)
    q3.put(3)
    
    assert out_q.get() == 1
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

pytutils/Test4DT_tests/test_pytutils_queues_merge_0.py F                 [100%]

=================================== FAILURES ===================================
_________________________ test_merge_with_three_queues _________________________

setup_queues = (<queue.Queue object at 0x7efc2f504a90>, <queue.Queue object at 0x7efc2e7be850>, <queue.Queue object at 0x7efc2e7bf1d0>)

    def test_merge_with_three_queues(setup_queues):
        q1, q2, q3 = setup_queues
        out_q = merge(q1, q2, q3)
    
        # Add elements to the queues
        q1.put(1)
        q2.put(2)
        q3.put(3)
    
>       assert out_q.get() == 1
E       assert 3 == 1
E        +  where 3 = get()
E        +    where get = <queue.Queue object at 0x7efc2e7bed50>.get

pytutils/Test4DT_tests/test_pytutils_queues_merge_0.py:32: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_queues_merge_0.py::test_merge_with_three_queues
============================== 1 failed in 0.05s ===============================
"""