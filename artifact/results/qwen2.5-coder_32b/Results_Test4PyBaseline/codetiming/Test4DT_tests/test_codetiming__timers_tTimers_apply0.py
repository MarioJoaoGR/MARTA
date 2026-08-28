
import pytest
from codetiming._timers import Timers
from typing import List, Callable
import statistics
import collections

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert list(timers._timings.keys()) == []

def test_apply_with_sum():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    result = timers.apply(sum, 'example_timer')
    assert result == pytest.approx(10.2)

def test_apply_with_mean():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    mean_time = timers.apply(lambda times: sum(times) / len(times), 'example_timer')
    assert mean_time == pytest.approx(3.4)

def test_apply_with_min():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    min_time = timers.apply(min, 'example_timer')
    assert min_time == pytest.approx(1.2)

def test_apply_with_max():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    max_time = timers.apply(max, 'example_timer')
    assert max_time == pytest.approx(5.6)

def test_apply_with_statistics_stdev():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    stdev_time = timers.apply(statistics.stdev, 'example_timer')