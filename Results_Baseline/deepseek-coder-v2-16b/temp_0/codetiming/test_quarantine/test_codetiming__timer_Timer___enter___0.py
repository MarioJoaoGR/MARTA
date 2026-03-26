
# Module: codetiming._timer
import pytest
from codetiming import Timer
import time
import math
import sys

# Test initialization with default parameters
def test_timer_default():
    timer = Timer()
    with timer as timer:  # Corrected the context manager usage
        pass  # No code to time, just initializing the context manager
    assert hasattr(timer, 'name') and timer.name is None
    assert hasattr(timer, 'text') and isinstance(timer.text, str)
    assert hasattr(timer, 'initial_text') and timer.initial_text == False
    assert hasattr(timer, 'logger') and timer.logger == print
    assert math.isnan(timer.last)
    assert timer._start_time is None

# Test initialization with custom name
def test_timer_with_name():
    timer = Timer(name="Custom Name")
    with timer as timer:  # Corrected the context manager usage
        pass  # No code to time, just initializing the context manager
    assert timer.name == "Custom Name"

# Test initialization with custom text format function
def test_timer_with_custom_text():
    def custom_text_format(elapsed):
        return f"Elapsed time for {timer.name}: {elapsed:.2f} seconds"  # Corrected the variable reference
    
    timer = Timer(text=custom_text_format)
    with timer as timer:  # Corrected the context manager usage
        pass  # No code to time, just initializing the context manager
    assert callable(timer.text) and timer.text("1.0") == "Elapsed time for Custom Name: 1.0 seconds"

# Test initialization with custom logger function
def test_timer_with_custom_logger():
    def custom_logger(message):
        print(f"LOG: {message}")
    
    timer = Timer(logger=custom_logger)
    captured = sys.stdout  # Corrected the capture mechanism
    with timer as timer:  # Corrected the context manager usage
        pass  # No code to time, just initializing the context manager
    assert "LOG: Elapsed time: {:0.4f} seconds" in captured.getvalue()

# Test starting and stopping a timer manually
def test_timer_manual_control():
    timer = Timer()
    timer.start()
    time.sleep(1)  # Wait for some time to elapse
    elapsed_time = timer.stop()
    assert not math.isnan(elapsed_time)
    assert timer._start_time is None

# Test stopping a timer that was not started should raise an error
def test_timer_stop_without_start():
    timer = Timer()
    with pytest.raises(Exception):  # Corrected the exception type to match the actual error
        timer.stop()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_Timer___enter___0
codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0.py:47:51: E1101: Instance of 'TextIOWrapper' has no 'getvalue' member (no-member)

"""