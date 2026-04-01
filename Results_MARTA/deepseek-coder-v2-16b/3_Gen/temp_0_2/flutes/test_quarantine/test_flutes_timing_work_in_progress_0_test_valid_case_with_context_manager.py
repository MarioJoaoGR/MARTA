
import pytest
from flutes.timing import work_in_progress
import time

@pytest.fixture(autouse=True)
def mock_time(monkeypatch):
    def mock_time_sleep():
        return 0
    
    monkeypatch.setattr(time, 'time', lambda: 1672531200 + (i * 0.1 for i in range(10)))
    monkeypatch.setattr(time, 'sleep', mock_time_sleep)

def test_valid_case_with_context_manager():
    with work_in_progress("Test task"):
        assert True  # Replace this with the actual assertion for your test case

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

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_context_manager.py F [100%]

=================================== FAILURES ===================================
_____________________ test_valid_case_with_context_manager _____________________

    def test_valid_case_with_context_manager():
>       with work_in_progress("Test task"):

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_context_manager.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/contextlib.py:137: in __enter__
    return next(self.gen)
flutes/flutes/timing.py:31: in work_in_progress
    begin_time = time.time()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

>   monkeypatch.setattr(time, 'time', lambda: 1672531200 + (i * 0.1 for i in range(10)))
E   TypeError: unsupported operand type(s) for +: 'int' and 'generator'

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_context_manager.py:11: TypeError
----------------------------- Captured stdout call -----------------------------
Test task... 
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_timing_work_in_progress_0_test_valid_case_with_context_manager.py::test_valid_case_with_context_manager
============================== 1 failed in 0.10s ===============================
"""