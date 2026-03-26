
import pytest
from codetiming import Timer, TimerError
import time
import math

# Test initialization of Timer with default parameters
def test_timer_initialization():
    timer = Timer()
    assert timer._start_time is None
    assert math.isnan(timer.last)
    assert timer.logger == print
    assert timer.text == 'Elapsed time: {:0.4f} seconds'
    assert not timer.initial_text

# Test starting the timer
def test_timer_start():
    timer = Timer()
    timer.start()
    assert isinstance(timer._start_time, float)

# Test stopping the timer without starting it should raise an error
def test_timer_stop_without_start():
    timer = Timer()
    with pytest.raises(TimerError):
        timer.stop()

# Test stopping the timer after starting it
def test_timer_stop():
    timer = Timer()
    timer.start()
    time.sleep(0.1)  # Sleep for a short period to ensure some time has passed
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time > 0

# Test stopping the timer with custom text format
def test_timer_stop_with_custom_text():
    def custom_text(elapsed):
        return f'Elapsed time: {elapsed:.2f} seconds'
    
    timer = Timer(text=custom_text)
    timer.start()
    time.sleep(0.1)  # Sleep for a short period to ensure some time has passed
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time > 0
    assert timer.text(elapsed_time) == 'Elapsed time: 0.10 seconds'

# Test stopping the timer with custom logger
def test_timer_stop_with_custom_logger():
    def custom_logger(message):
        print(f"LOG: {message}")
    
    timer = Timer(logger=custom_logger)
    timer.start()
    time.sleep(0.1)  # Sleep for a short period to ensure some time has passed
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time > 0
    assert hasattr(custom_logger, 'call_count') and getattr(custom_logger, 'call_count', 0) == 1

# Test stopping the timer with name and reporting it in timers
def test_timer_stop_with_name():
    timer = Timer(name="TestTimer")
    timer.start()
    time.sleep(0.1)  # Sleep for a short period to ensure some time has passed
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time > 0
    assert "TestTimer" in timer.timers._timers
    assert timer.timers._timers["TestTimer"] == elapsed_time

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_Timer_stop_0
codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_0.py:71:26: E1101: Instance of 'Timers' has no '_timers' member (no-member)
codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_0.py:72:11: E1101: Instance of 'Timers' has no '_timers' member (no-member)

"""