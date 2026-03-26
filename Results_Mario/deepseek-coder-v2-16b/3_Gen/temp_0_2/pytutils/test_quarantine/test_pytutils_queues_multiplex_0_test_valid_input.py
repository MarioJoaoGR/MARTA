
import pytest
from queue import Queue
from pytutils.queues import multiplex

def test_valid_input():
    in_q = Queue()
    q1, q2, q3 = multiplex(in_q, count=3)

    # Add items to the input queue
    in_q.put("item1")
    in_q.put("item2")

    # Check if items are present in all output queues
    assert not q1.empty()
    assert not q2.empty()
    assert not q3.empty()

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
        q1, q2, q3 = multiplex(in_q, count=3)
    
        # Add items to the input queue
        in_q.put("item1")
        in_q.put("item2")
    
        # Check if items are present in all output queues
>       assert not q1.empty()
E       assert not True
E        +  where True = empty()
E        +    where empty = <queue.Queue object at 0x7fad92ac6f90>.empty

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""