
import pytest
from codetiming import Timer
from typing import Optional, Union, Callable
import math
import time

class TimerError(Exception):
    """A custom exception used to report timer errors."""
    pass

def test_timer():
    with pytest.raises(TimerError) as excinfo:
        # Attempting to start a new timer while it's already running should raise an error
        with Timer() as t1:
            with Timer() as t2:  # This should raise an error because the first timer is still running
                pass
    assert str(excinfo.value) == "Timer is already running."

def test_timer_with_custom_name():
    with pytest.raises(TimerError) as excinfo:
        # Attempting to start a new timer while it's already running should raise an error
        with Timer(name="Custom Name") as t1:
            with Timer(name="Another Custom Name") as t2:  # This should raise an error because the first timer is still running
                pass
    assert str(excinfo.value) == "Timer is already running."

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________________ test_timer __________________________________

    def test_timer():
>       with pytest.raises(TimerError) as excinfo:
E       Failed: DID NOT RAISE <class 'Test4DT_tests.test_codetiming__timer_Timer___enter___0_test_edge_cases.TimerError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_edge_cases.py:13: Failed
----------------------------- Captured stdout call -----------------------------
Elapsed time: 0.0000 seconds
Elapsed time: 0.0000 seconds
_________________________ test_timer_with_custom_name __________________________

    def test_timer_with_custom_name():
>       with pytest.raises(TimerError) as excinfo:
E       Failed: DID NOT RAISE <class 'Test4DT_tests.test_codetiming__timer_Timer___enter___0_test_edge_cases.TimerError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_edge_cases.py:21: Failed
----------------------------- Captured stdout call -----------------------------
Elapsed time: 0.0000 seconds
Elapsed time: 0.0000 seconds
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_edge_cases.py::test_timer
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_edge_cases.py::test_timer_with_custom_name
============================== 2 failed in 0.02s ===============================
"""