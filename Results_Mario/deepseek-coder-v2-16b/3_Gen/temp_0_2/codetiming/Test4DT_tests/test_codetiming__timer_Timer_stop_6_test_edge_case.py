
import pytest
from codetiming import Timer
from codetiming._timer import TimerError
import time

@pytest.fixture
def timer():
    return Timer()

def test_stop_when_not_started(timer):
    with pytest.raises(TimerError) as excinfo:
        timer.stop()
    assert str(excinfo.value) == "Timer is not running. Use .start() to start it"

def test_stop_with_valid_timing(timer):
    timer._start_time = time.perf_counter() - 1  # Mock the start time
    elapsed_time = timer.stop()
    assert isinstance(elapsed_time, float)
    assert elapsed_time > 0
