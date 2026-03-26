
import pytest
from pytutils.queues import multiplex
from queue import Queue

def test_error_handling():
    with pytest.raises(TypeError):
        in_q = 'invalid'
        count = 'invalid'
        try:
            q1, q2 = multiplex(in_q, count)
        except TypeError as e:
            assert str(e) == "Expected a queue object for input `q`, but got <class 'str'>"

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

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        with pytest.raises(TypeError):
            in_q = 'invalid'
            count = 'invalid'
            try:
>               q1, q2 = multiplex(in_q, count)

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_error_handling.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

q = 'invalid', count = 'invalid'
queue_factory = <function <lambda> at 0x7f537c7b4b80>

    def multiplex(q, count=2, queue_factory=lambda: Queue()):
        """ Convert one queue into several. Kind of like a teeing queue.
    
        >>> in_q = Queue()
        >>> q1, q2, q3 = multiplex(in_q, count=3)
        """
>       out_queues = [queue_factory() for _ in range(count)]
E       TypeError: 'str' object cannot be interpreted as an integer

pytutils/pytutils/queues.py:11: TypeError

During handling of the above exception, another exception occurred:

    def test_error_handling():
        with pytest.raises(TypeError):
            in_q = 'invalid'
            count = 'invalid'
            try:
                q1, q2 = multiplex(in_q, count)
            except TypeError as e:
>               assert str(e) == "Expected a queue object for input `q`, but got <class 'str'>"
E               assert "'str' object...as an integer" == "Expected a q...<class 'str'>"
E                 
E                 - Expected a queue object for input `q`, but got <class 'str'>
E                 + 'str' object cannot be interpreted as an integer

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_error_handling.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_error_handling.py::test_error_handling
============================== 1 failed in 0.06s ===============================
"""