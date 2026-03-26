
import pytest
from codetiming import Timer
from codetiming._timer import TimerError
import time

@pytest.fixture
def timer():
    return Timer()

def test_stop_with_no_start(timer):
    with pytest.raises(TimerError) as excinfo:
        timer.stop()
    assert str(excinfo.value) == "Timer is not running. Use .start() to start it"

def test_stop_after_start(timer):
    timer._start_time = time.perf_counter() - 0.1
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time > 0
