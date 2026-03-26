
import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_error_handling():
    timer = Timer()
    with pytest.raises(TimerError):
        timer.__exit__()
