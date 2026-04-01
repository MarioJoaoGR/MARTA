
import pytest
from flutes.multiproc import safe_pool
from multiprocessing import Pool
from typing import Type, Tuple, Any, Optional, List

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Providing incorrect types for the parameters should raise a TypeError
        safe_pool("not an int", "extra argument", state_class=Pool, init_args=(), closing=[], suppress_exceptions=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_invalid_inputs.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.12s ===============================
"""