
import pytest
from codetiming import Timer
from typing import Optional, Union, Callable, ClassVar
from dataclasses import field
import math
import time

class Timers:
    def add(self, name: str, elapsed_time: float):
        pass

class TimerError(Exception):
    pass

def test_stop():
    timer = Timer()
    with pytest.raises(TimerError) as excinfo:
        timer.stop()
    assert str(excinfo.value) == "Timer is not running. Use .start() to start it"

    # Mock the necessary attributes and methods for a successful test
    timer._start_time = time.perf_counter() - 0.1
    elapsed_time = timer.stop()
    assert math.isclose(elapsed_time, 0.1, abs_tol=0.01)

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_stop ___________________________________

    def test_stop():
        timer = Timer()
        with pytest.raises(TimerError) as excinfo:
>           timer.stop()

codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_1_test_edge_case.py:19: 
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
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_1_test_edge_case.py::test_stop
============================== 1 failed in 0.02s ===============================
"""