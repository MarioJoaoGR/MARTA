
import pytest
from flutes.timing import work_in_progress

def test_valid_case_with_function_decoration():
    @work_in_progress("Test task")
    def dummy_function():
        pass
    
    # Mock the time to control the elapsed time for testing
    with pytest.raises(StopIteration):
        dummy_function()

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
        @work_in_progress("Test task")
        def dummy_function():
            pass
    
        # Mock the time to control the elapsed time for testing
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_function_decoration.py:11: Failed
----------------------------- Captured stdout call -----------------------------
Test task... done. (0.00s)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_function_decoration.py::test_valid_case_with_function_decoration
============================== 1 failed in 0.08s ===============================
"""