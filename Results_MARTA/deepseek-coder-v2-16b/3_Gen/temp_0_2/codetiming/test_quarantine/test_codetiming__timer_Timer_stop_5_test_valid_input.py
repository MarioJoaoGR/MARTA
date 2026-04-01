
import pytest
from codetiming import Timer
from typing import Optional, Union, Callable, ClassVar
from dataclasses import field
import math
import time

class TimerError(Exception):
    """A custom exception used to report errors in use of the Timer class"""
    pass

class Timers:
    def add(self, name: str, elapsed_time: float) -> None:
        pass

# Assuming you have a module named 'your_module' which contains the Timer class definition.
# from your_module import Timer

def test_valid_input():
    timer = Timer()
    with pytest.raises(TimerError):
        assert timer.stop()
    
    # Start the timer
    timer._start_time = time.perf_counter()
    
    # Stop the timer and get the elapsed time
    elapsed_time = timer.stop()
    
    # Check if the elapsed time is a float
    assert isinstance(elapsed_time, float)
    
    # Check if the logger function is called with the correct message
    import io
    from unittest.mock import patch
    
    captured_output = io.StringIO()
    with patch('sys.stdout', new=captured_output):
        timer.logger = print
        assert timer.stop() == elapsed_time  # Ensure stop returns the same value after starting
        assert captured_output.getvalue().strip() == f"Elapsed time: {elapsed_time} seconds"

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_5_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        timer = Timer()
        with pytest.raises(TimerError):
>           assert timer.stop()

codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_5_test_valid_input.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text=False, logger=<built-in function print>)

    def stop(self) -> float:
        """Stop the timer, and report the elapsed time."""
        if self._start_time is None:
>           raise TimerError("Timer is not running. Use .start() to start it")
E           codetiming._timer.TimerError: Timer is not running. Use .start() to start it

codetiming/codetiming/_timer.py:74: TimerError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_5_test_valid_input.py::test_valid_input
============================== 1 failed in 0.02s ===============================
"""