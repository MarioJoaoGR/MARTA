
import pytest
from queue import Queue
from pytutils.queues import multiplex

def test_edge_case_none():
    with pytest.raises(TypeError):
        q = None
        out_queues = multiplex(q)

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

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_edge_case_none.py:7: Failed
=============================== warnings summary ===============================
Test4DT_tests/test_pytutils_queues_multiplex_0_test_edge_case_none.py::test_edge_case_none
  /usr/local/lib/python3.11/site-packages/_pytest/threadexception.py:82: PytestUnhandledThreadExceptionWarning: Exception in thread Thread-1 (f)
  
  Traceback (most recent call last):
    File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
      self.run()
    File "/usr/local/lib/python3.11/threading.py", line 982, in run
      self._target(*self._args, **self._kwargs)
    File "/projects/F202407648IACDCF2/mario/pytutils/pytutils/queues.py", line 15, in f
      x = q.get()
          ^^^^^
  AttributeError: 'NoneType' object has no attribute 'get'
  
    warnings.warn(pytest.PytestUnhandledThreadExceptionWarning(msg))

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_edge_case_none.py::test_edge_case_none
========================= 1 failed, 1 warning in 0.06s =========================
"""