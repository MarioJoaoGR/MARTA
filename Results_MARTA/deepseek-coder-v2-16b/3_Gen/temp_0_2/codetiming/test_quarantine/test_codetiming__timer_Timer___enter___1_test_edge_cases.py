
import pytest
from codetiming import Timer
from typing import Optional, Union, Callable
import math
import time

class TimerError(Exception):
    """A custom exception used to report errors in using Timer."""
    pass

def test_timer_context_manager():
    with pytest.raises(TimerError) as exc_info:
        with Timer() as timer:  # This should raise an error because the timer is already running
            pass
    assert str(exc_info.value) == "Timer is already running."

def test_timer_context_manager_with_name():
    with pytest.raises(TimerError) as exc_info:
        with Timer(name="test") as timer:  # This should raise an error because the timer is already running
            pass
    assert str(exc_info.value) == "Timer is already running."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/codetiming
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___1_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_timer_context_manager __________________________

    def test_timer_context_manager():
>       with pytest.raises(TimerError) as exc_info:
E       Failed: DID NOT RAISE <class 'Test4DT_tests.test_codetiming__timer_Timer___enter___1_test_edge_cases.TimerError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___1_test_edge_cases.py:13: Failed
----------------------------- Captured stdout call -----------------------------
Elapsed time: 0.0000 seconds
_____________________ test_timer_context_manager_with_name _____________________

    def test_timer_context_manager_with_name():
>       with pytest.raises(TimerError) as exc_info:
E       Failed: DID NOT RAISE <class 'Test4DT_tests.test_codetiming__timer_Timer___enter___1_test_edge_cases.TimerError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___1_test_edge_cases.py:19: Failed
----------------------------- Captured stdout call -----------------------------
Elapsed time: 0.0000 seconds
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___1_test_edge_cases.py::test_timer_context_manager
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___1_test_edge_cases.py::test_timer_context_manager_with_name
============================== 2 failed in 0.02s ===============================
"""