
import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_valid_input():
    timer = Timer()
    with pytest.raises(TimerError):
        assert timer.stop()
