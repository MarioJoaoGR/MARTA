
import pytest
from codetiming import Timer
from time import perf_counter
import math

class TimerError(Exception):
    """A custom exception used for timer errors."""
    pass

def test_valid_input():
    timer = Timer()
    assert timer._start_time is None
    
    # Start the timer
    timer.start()
    assert isinstance(timer._start_time, float)
    
    # Wait for a short period to ensure some time has passed
    import time
    time.sleep(0.1)
    
    # Stop the timer and get the elapsed time
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time >= 0.1
    assert timer._start_time is None
