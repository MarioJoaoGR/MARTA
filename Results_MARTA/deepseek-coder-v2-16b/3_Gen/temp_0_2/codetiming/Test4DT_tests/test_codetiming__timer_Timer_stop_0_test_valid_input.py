
import pytest
from typing import Optional, Union, Callable
from codetiming._timer import Timer
import math
import time

class MockTimer(Timer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._start_time = None
        self.last = 0.0

def test_valid_input():
    timer = MockTimer()
    assert isinstance(timer, Timer), "Instance should be an instance of Timer"
    
    # Start the timer
    timer.start()
    time.sleep(1)  # Sleep for a second to ensure some elapsed time
    
    # Stop the timer and get the elapsed time
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float), "Elapsed time should be a float"
    assert elapsed_time > 0, "Elapsed time should be greater than zero"
