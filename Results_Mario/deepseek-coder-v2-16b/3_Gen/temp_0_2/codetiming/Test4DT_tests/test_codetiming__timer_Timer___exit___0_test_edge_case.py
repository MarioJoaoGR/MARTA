
import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_stop():
    timer = Timer()
    with pytest.raises(TimerError):
        elapsed_time = timer.stop()
