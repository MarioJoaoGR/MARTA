
import pytest
from codetiming import Timer
import time
import math

# Define the TimerError exception class
class TimerError(Exception):
    """A custom exception used to signal timer errors."""
    pass

def test_invalid_inputs():
    # Create an instance of the Timer class
    timer = Timer()
    
    # Test that starting a running timer raises a TimerError
    with pytest.raises(TimerError):
        timer._start_time = time.perf_counter()  # Simulate the timer being already started
        timer.start()

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Create an instance of the Timer class
        timer = Timer()
    
        # Test that starting a running timer raises a TimerError
        with pytest.raises(TimerError):
            timer._start_time = time.perf_counter()  # Simulate the timer being already started
>           timer.start()

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_invalid_inputs.py:19: 
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
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================
"""