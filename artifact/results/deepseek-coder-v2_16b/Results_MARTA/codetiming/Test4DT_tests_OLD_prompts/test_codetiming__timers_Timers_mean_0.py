
import pytest
from codetiming._timers import Timers
import statistics
from typing import List, Callable

# Test for adding timings to a timer and applying a function to it
def test_apply_function():
    timers = Timers()
    timers.add('task1', 1.23)
    timers.add('task1', 4.56)
    result = timers.apply(lambda x: sum(x), 'task1')
    assert result == pytest.approx(5.79, rel=1e-9)

# Test for applying a function to a non-existent timer
def test_apply_no_timings():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), 'non_existent_task')

# Test for calculating the mean of timings from an empty list (should return 0)
def test_mean_empty_list():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.mean('non_existent_task')
