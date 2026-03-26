
import pytest
from multiprocessing import Pool
from flutes.multiproc import safe_pool

def test_valid_inputs():
    # Test with default parameters
    pool = safe_pool(processes=4)
    assert isinstance(pool, Pool), "Expected a Pool object"

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

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test with default parameters
        pool = safe_pool(processes=4)
>       assert isinstance(pool, Pool), "Expected a Pool object"
E       TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_valid_inputs.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""