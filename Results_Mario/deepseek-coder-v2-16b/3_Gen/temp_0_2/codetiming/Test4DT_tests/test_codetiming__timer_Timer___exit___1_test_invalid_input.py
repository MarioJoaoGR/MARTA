
import pytest
from codetiming._timer import Timer
from codetiming._timer import TimerError

def test_invalid_input():
    timer = Timer()
    with pytest.raises(TimerError):
        timer.stop()
