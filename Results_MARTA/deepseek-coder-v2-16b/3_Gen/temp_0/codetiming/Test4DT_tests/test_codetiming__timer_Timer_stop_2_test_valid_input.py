
import pytest
from codetiming import Timer
from codetiming._timer import TimerError
import time

def test_stop():
    timer = Timer()
    
    # Test that stop raises TimerError if the timer has not been started
    with pytest.raises(TimerError) as excinfo:
        timer.stop()
