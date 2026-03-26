
import pytest
from collections import deque
from pytutils.queues import push

def test_invalid_inputs():
    # Setup
    in_q = deque()
    out_q = 'not a queue'
    
    # Test with invalid types for input and output queues
    with pytest.raises(TypeError):
        push(in_q, out_q)

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

pytutils/Test4DT_tests/test_pytutils_queues_push_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Setup
        in_q = deque()
        out_q = 'not a queue'
    
        # Test with invalid types for input and output queues
        with pytest.raises(TypeError):
>           push(in_q, out_q)

pytutils/Test4DT_tests/test_pytutils_queues_push_0_test_invalid_inputs.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

in_q = deque([]), out_q = 'not a queue'

    def push(in_q, out_q):
        while True:
>           x = in_q.get()
E           AttributeError: 'collections.deque' object has no attribute 'get'

pytutils/pytutils/queues.py:27: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_queues_push_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.06s ===============================
"""