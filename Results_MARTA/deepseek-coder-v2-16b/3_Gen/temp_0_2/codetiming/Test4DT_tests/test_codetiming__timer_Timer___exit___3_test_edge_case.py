
import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_exit():
    timer = Timer()
    with pytest.raises(TimerError):
        timer.__exit__(None, None, None)
