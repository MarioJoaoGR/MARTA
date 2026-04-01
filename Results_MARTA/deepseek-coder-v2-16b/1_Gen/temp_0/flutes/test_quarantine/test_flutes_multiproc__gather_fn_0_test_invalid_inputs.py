
import pytest
from multiprocessing import Queue
from flutes.multiproc import _gather_fn, END_SIGNATURE
from typing import Callable, Iterator, Optional, Type

def test_invalid_inputs():
    q = Queue()
    with pytest.raises(Exception):
        def faulty_fn():
            raise Exception("Faulty function")
        _gather_fn(q, faulty_fn)

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

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        q = Queue()
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_invalid_inputs.py:9: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-24 16:44:03] Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
             ^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_invalid_inputs.py", line 11, in faulty_fn
    raise Exception("Faulty function")
Exception: Faulty function

[2026-03-24 16:44:03] <Exception> Faulty function
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
             ^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_invalid_inputs.py", line 11, in faulty_fn
    raise Exception("Faulty function")
Exception: Faulty function

ERROR    flutes.log:log.py:182 <Exception> Faulty function
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.09s ===============================
"""