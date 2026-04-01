
import pytest
from codetiming import Timer
import time
import math

# Define a custom exception for testing the error handling in the start method
class TimerError(Exception):
    pass

def test_valid_input():
    timer = Timer()
    
    # Test that starting a new timer raises an error if it's already running
    with pytest.raises(TimerError):
        timer.start()
        timer.start()  # Attempt to start again should raise TimerError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/codetiming
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        timer = Timer()
    
        # Test that starting a new timer raises an error if it's already running
        with pytest.raises(TimerError):
            timer.start()
>           timer.start()  # Attempt to start again should raise TimerError

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_valid_input.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text=False, logger=<built-in function print>)

    def start(self) -> None:
        """Start a new timer."""
        if self._start_time is not None:
>           raise TimerError("Timer is running. Use .stop() to stop it")
E           codetiming._timer.TimerError: Timer is running. Use .stop() to stop it

codetiming/codetiming/_timer.py:57: TimerError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.02s ===============================
"""