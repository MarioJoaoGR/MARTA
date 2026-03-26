
import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_valid_input():
    timer = Timer()
    
    # Test that starting a new timer raises an error if it's already running
    with pytest.raises(TimerError):
        timer.start()  # First start should be fine
        timer.start()   # Second start should raise TimerError
