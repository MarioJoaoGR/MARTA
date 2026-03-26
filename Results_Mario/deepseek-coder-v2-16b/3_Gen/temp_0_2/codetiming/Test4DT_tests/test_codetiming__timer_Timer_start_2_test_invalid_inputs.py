
import pytest
from codetiming import Timer
from codetiming._timer import TimerError
import time

def test_invalid_inputs():
    # Create an instance of the Timer class
    timer = Timer()
    
    # Test that starting a running timer raises a TimerError
    with pytest.raises(TimerError):
        timer._start_time = time.perf_counter()  # Simulate the timer being already started
        timer.start()
