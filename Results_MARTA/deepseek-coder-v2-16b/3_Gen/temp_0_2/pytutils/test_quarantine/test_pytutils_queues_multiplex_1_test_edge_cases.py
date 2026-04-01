
import pytest
from queue import Queue
from pytutils.queues import multiplex
from threading import Thread

def test_edge_cases():
    in_q = Queue()
    
    # Test with None count
    q1, q2 = multiplex(in_q, count=None)
    assert len(multiplex(in_q, count=None)) == 2, "Expected two queues when count is None"
    
    # Test with zero count
    q3, q4 = multiplex(in_q, count=0)
    assert len(multiplex(in_q, count=0)) == 0, "Expected no queues when count is zero"

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

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        in_q = Queue()
    
        # Test with None count
>       q1, q2 = multiplex(in_q, count=None)

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_1_test_edge_cases.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

q = <queue.Queue object at 0x7f63f123d6d0>, count = None
queue_factory = <function <lambda> at 0x7f63f1151c60>

    def multiplex(q, count=2, queue_factory=lambda: Queue()):
        """ Convert one queue into several. Kind of like a teeing queue.
    
        >>> in_q = Queue()
        >>> q1, q2, q3 = multiplex(in_q, count=3)
        """
>       out_queues = [queue_factory() for _ in range(count)]
E       TypeError: 'NoneType' object cannot be interpreted as an integer

pytutils/pytutils/queues.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_queues_multiplex_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.06s ===============================
"""