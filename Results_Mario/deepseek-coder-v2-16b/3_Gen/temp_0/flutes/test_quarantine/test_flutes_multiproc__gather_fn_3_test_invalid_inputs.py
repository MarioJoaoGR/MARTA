
import pytest
from multiprocessing import Queue
from typing import Callable, Iterator, Optional, Type
from flutes.multiproc import _gather_fn, END_SIGNATURE

def test_invalid_inputs():
    # Create a mock queue and function
    q = Queue()
    
    def example_fn(x):
        yield x * 2
        yield x * 3
    
    # Test with invalid inputs (None for fn)
    with pytest.raises(TypeError):
        _gather_fn(q, None)  # Passing None instead of a callable function should raise TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_3_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Create a mock queue and function
        q = Queue()
    
        def example_fn(x):
            yield x * 2
            yield x * 3
    
        # Test with invalid inputs (None for fn)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_3_test_invalid_inputs.py:16: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-22 21:35:38] Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
             ^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable

[2026-03-22 21:35:38] <TypeError> 'NoneType' object is not callable
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
             ^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable

ERROR    flutes.log:log.py:182 <TypeError> 'NoneType' object is not callable
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_3_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""