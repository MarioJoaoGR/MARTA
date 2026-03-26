
import pytest
from codetiming import Timer
from time import perf_counter

@pytest.fixture
def timer():
    return Timer()

def test_stop_valid_input(timer):
    # Start the timer
    timer._start_time = perf_counter() - 0.1
    
    # Stop the timer and get the elapsed time
    elapsed_time = timer.stop()
    
    # Check if the elapsed time is correct
    assert isinstance(elapsed_time, float)
    assert elapsed_time >= 0.1
