
import pytest
from flutes.timing import work_in_progress
import time

def test_valid_case_with_function_decoration():
    @work_in_progress("Test Function")
    def target_function():
        time.sleep(1)  # Simulate a task that takes 1 second to complete
    
    with pytest.raises(RuntimeError, match="yield statement missing"):
        target_function()

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

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_function_decoration.py F [100%]

=================================== FAILURES ===================================
___________________ test_valid_case_with_function_decoration ___________________

    def test_valid_case_with_function_decoration():
        @work_in_progress("Test Function")
        def target_function():
            time.sleep(1)  # Simulate a task that takes 1 second to complete
    
>       with pytest.raises(RuntimeError, match="yield statement missing"):
E       Failed: DID NOT RAISE <class 'RuntimeError'>

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_function_decoration.py:11: Failed
----------------------------- Captured stdout call -----------------------------
Test Function... done. (1.00s)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_function_decoration.py::test_valid_case_with_function_decoration
============================== 1 failed in 1.09s ===============================
"""