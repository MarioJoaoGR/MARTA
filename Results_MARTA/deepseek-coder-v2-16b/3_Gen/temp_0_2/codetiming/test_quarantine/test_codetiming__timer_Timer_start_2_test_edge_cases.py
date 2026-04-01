
import pytest
from codetiming import Timer
import time
import math

def test_start_with_none_initial_text():
    timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text=None, logger=print)
    with pytest.raises(TypeError):
        timer.start()

def test_start_with_empty_string_initial_text():
    timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=print)
    with pytest.raises(ValueError):
        timer.start()

def test_start_with_default_initial_text():
    timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=print)
    with pytest.raises(TypeError):
        timer.start()

def test_start_with_invalid_logger():
    timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=None)
    with pytest.raises(AttributeError):
        timer.start()

def test_start_when_already_running():
    timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=None)
    timer._start_time = time.perf_counter()
    with pytest.raises(RuntimeError):
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
collected 5 items

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
______________________ test_start_with_none_initial_text _______________________

    def test_start_with_none_initial_text():
        timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text=None, logger=print)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py:9: Failed
__________________ test_start_with_empty_string_initial_text ___________________

    def test_start_with_empty_string_initial_text():
        timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=print)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py:14: Failed
_____________________ test_start_with_default_initial_text _____________________

    def test_start_with_default_initial_text():
        timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=print)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py:19: Failed
________________________ test_start_with_invalid_logger ________________________

    def test_start_with_invalid_logger():
        timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=None)
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py:24: Failed
_______________________ test_start_when_already_running ________________________

    def test_start_when_already_running():
        timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=None)
        timer._start_time = time.perf_counter()
        with pytest.raises(RuntimeError):
>           timer.start()

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text='', logger=None)

    def start(self) -> None:
        """Start a new timer."""
        if self._start_time is not None:
>           raise TimerError("Timer is running. Use .stop() to stop it")
E           codetiming._timer.TimerError: Timer is running. Use .stop() to stop it

codetiming/codetiming/_timer.py:57: TimerError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py::test_start_with_none_initial_text
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py::test_start_with_empty_string_initial_text
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py::test_start_with_default_initial_text
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py::test_start_with_invalid_logger
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_2_test_edge_cases.py::test_start_when_already_running
============================== 5 failed in 0.02s ===============================
"""