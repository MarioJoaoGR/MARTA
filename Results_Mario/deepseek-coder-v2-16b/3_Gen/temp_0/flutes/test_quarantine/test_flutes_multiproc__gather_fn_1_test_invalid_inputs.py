
import pytest
from multiprocessing import Queue
from typing import Callable, Iterator, Optional, Type
from flutes.multiproc import _gather_fn, END_SIGNATURE

def test_invalid_inputs():
    q = Queue()
    with pytest.raises(Exception):
        # Test that an invalid function raises an Exception
        def invalid_fn(*args, **kwargs):
            yield None  # This should be a generator function to match the signature of _gather_fn's fn parameter
        
        _gather_fn(q, invalid_fn)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        q = Queue()
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_1_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""