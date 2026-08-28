
import pytest
from codetiming._timers import Timers
import math

def test_stdev_with_multiple_recordings():
    timers = Timers()
    timers._timings['example'] = [1.0, 2.0, 3.0]
    assert math.isclose(timers.stdev('example'), 1.0)

def test_stdev_with_two_recordings():
    timers = Timers()
    timers._timings['example'] = [1.0, 2.0]
    assert math.isclose(timers.stdev('example'), 0.7071067811865476)

def test_stdev_with_one_recording():
    timers = Timers()
    timers._timings['example'] = [1.0]
    assert math.isnan(timers.stdev('example'))

def test_stdev_with_no_recordings():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('non_existent')

def test_stdev_with_empty_list():
    timers = Timers()
    timers._timings['empty'] = []
    assert math.isnan(timers.stdev('empty'))

def test_stdev_with_identical_recordings():
    timers = Timers()
    timers._timings['identical'] = [2.0, 2.0, 2.0]
    assert math.isclose(timers.stdev('identical'), 0.0)
