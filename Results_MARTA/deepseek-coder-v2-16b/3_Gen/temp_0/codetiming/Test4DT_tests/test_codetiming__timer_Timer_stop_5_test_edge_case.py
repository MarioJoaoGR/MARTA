
import pytest
from codetiming import Timer
from codetiming._timer import TimerError
import time

def test_stop():
    timer = Timer()
    with pytest.raises(TimerError):
        timer.stop()
