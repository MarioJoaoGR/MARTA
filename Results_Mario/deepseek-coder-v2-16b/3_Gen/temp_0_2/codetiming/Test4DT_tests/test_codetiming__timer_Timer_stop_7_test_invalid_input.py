
import pytest
from codetiming import Timer
from codetiming._timer import TimerError
import time

def test_invalid_input():
    timer = Timer()
    with pytest.raises(TimerError):
        assert timer.stop()
