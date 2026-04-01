
import pytest
from codetiming._timers import Timers  # Correctly importing from the module
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_median_empty(timers):
    with pytest.raises(KeyError):
        timers.median('non_existent_timer')

def test_median_single_value(timers):
    timers._timings['test_timer'] = [1.0]
    assert timers.median('test_timer') == 1.0

def test_median_multiple_values(timers):
    timers._timings['test_timer'] = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert timers.median('test_timer') == 3.0

def test_median_zero_values(timers):
    timers._timings['test_timer'] = []
    assert timers.median('test_timer') == 0
