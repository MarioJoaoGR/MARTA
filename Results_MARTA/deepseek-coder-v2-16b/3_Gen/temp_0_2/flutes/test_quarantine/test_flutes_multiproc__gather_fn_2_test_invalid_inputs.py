
import pytest
from multiprocessing import Queue
from typing import Callable, Iterator, Optional, Type
from flutes.multiproc import _gather_fn, END_SIGNATURE

def test_invalid_inputs():
    q = Queue()
    fn = lambda: iter([1, 2, 3])
    
    with pytest.raises(TypeError):
        _gather_fn(q, fn)

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

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        q = Queue()
        fn = lambda: iter([1, 2, 3])
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_2_test_invalid_inputs.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.10s ===============================
"""