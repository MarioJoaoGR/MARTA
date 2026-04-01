
import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_stop():
    timer = Timer()
    with pytest.raises(TimerError) as excinfo:
        timer.stop()
    assert str(excinfo.value) == "Timer is not running. Use .start() to start it"
