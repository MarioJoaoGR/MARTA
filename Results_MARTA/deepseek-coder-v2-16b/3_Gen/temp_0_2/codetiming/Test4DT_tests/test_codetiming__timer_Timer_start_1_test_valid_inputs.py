
import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_valid_inputs():
    timer = Timer()
    with pytest.raises(TimerError):
        # First start the timer
        timer.start()
        # Attempt to start it again, which should raise a TimerError
        timer.start()
