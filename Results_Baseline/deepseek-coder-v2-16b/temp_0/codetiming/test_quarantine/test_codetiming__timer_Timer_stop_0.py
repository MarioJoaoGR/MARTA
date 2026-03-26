
# Module: codetiming._timer
import pytest
from codetiming import Timer
import time
import math

# Test default initialization of Timer
def test_default_initialization():
    timer = Timer()
    with timer:
        # Simulate some code execution
        time.sleep(0.1)
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float), "Elapsed time should be a float"
    assert 0.09 < elapsed_time < 0.2, "Elapsed time should be approximately 0.1 seconds"

# Test custom name for Timer
def test_custom_name():
    timer = Timer(name="Custom Name")
    with timer:
        # Simulate some code execution
        time.sleep(0.1)
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float), "Elapsed time should be a float"
    assert 0.09 < elapsed_time < 0.2, "Elapsed time should be approximately 0.1 seconds"

# Test custom text format for Timer
def test_custom_text_format():
    def custom_text_format(elapsed):
        return f"Custom Elapsed time: {elapsed:.2f} seconds"
    
    timer = Timer(text=custom_text_format)
    with timer:
        # Simulate some code execution
        time.sleep(0.1)
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float), "Elapsed time should be a float"
    assert 0.09 < elapsed_time < 0.2, "Elapsed time should be approximately 0.1 seconds"
    expected_text = custom_text_format(elapsed_time)
    assert timer.logger is not None, "Logger function should be set"
    assert callable(timer.logger), "Logger function should be callable"
    assert timer.logger(expected_text) is None, "Logger function should log the expected text"

# Test custom logger function for Timer
def test_custom_logger(capsys):
    def custom_logger(message):
        print(f"LOG: {message}")
    
    timer = Timer(logger=custom_logger)
    with timer:
        # Simulate some code execution
        time.sleep(0.1)
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float), "Elapsed time should be a float"
    assert 0.09 < elapsed_time < 0.2, "Elapsed time should be approximately 0.1 seconds"
    expected_log = f"LOG: {timer.text(elapsed_time)}"
    captured_output = capsys.readouterr()
    assert expected_log in captured_output.out, "Logger function should log the formatted elapsed time"

# Test handling exceptions when stopping an unstarted timer
def test_stop_unstarted_timer():
    timer = Timer()
    with pytest.raises(TimerError) as excinfo:
        timer.stop()
    assert str(excinfo.value) == "Timer is not running. Use .start() to start it"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_Timer_stop_0
codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_0.py:64:23: E0602: Undefined variable 'TimerError' (undefined-variable)

"""