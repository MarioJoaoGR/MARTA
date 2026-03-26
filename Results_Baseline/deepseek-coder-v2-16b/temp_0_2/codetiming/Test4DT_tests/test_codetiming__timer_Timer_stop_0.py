
# Module: codetiming._timer
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
    assert timer._start_time is not None

# Test stopping the timer without custom parameters
def test_timer_stop_without_custom_parameters():
    timer = Timer()
    timer.start()
    time.sleep(0.1)  # Sleep for a short period to ensure some time has passed
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time > 0
    assert math.isclose(elapsed_time, 0.1, abs_tol=0.01)

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
    assert custom_text(elapsed_time) == 'Elapsed time: {:.2f} seconds'.format(elapsed_time)

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
    assert custom_logger('LOG: Elapsed time: {:.2f} seconds'.format(elapsed_time)) is None

# Test stopping the timer with name and reporting it in timers
def test_timer_stop_with_name():
    timer = Timer(name="TestTimer")
    timer.start()
    time.sleep(0.1)  # Sleep for a short period to ensure some time has passed
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time > 0
    assert "TestTimer" in timer.timers.data
    assert math.isclose(timer.timers.data["TestTimer"], 0.1, abs_tol=0.01)
