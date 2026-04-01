
import pytest
from pytutils.iters import dedupe

def test_invalid_input():
    # Define a function that returns an invalid input (e.g., not iterable)
    def invalid_func():
        return 123
    
    # Use the dedupe decorator with the invalid function
    with pytest.raises(TypeError):
        dedupe(invalid_func, instance=None, args=(), kwargs={})

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

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Define a function that returns an invalid input (e.g., not iterable)
        def invalid_func():
            return 123
    
        # Use the dedupe decorator with the invalid function
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_invalid_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""