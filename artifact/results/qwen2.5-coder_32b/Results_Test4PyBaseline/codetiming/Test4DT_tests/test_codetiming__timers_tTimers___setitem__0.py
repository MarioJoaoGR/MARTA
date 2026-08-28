
# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import collections  # Importing collections to use defaultdict
import math         # Importing math to use isnan

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert list(timers._timings.keys()) == []

def test_timers_adding_times():
    timers = Timers()
    timers._timings['load_data'].append(0.5)
    timers._timings['process_data'].append(1.2)
    assert timers._timings['load_data'] == [0.5]
    assert timers._timings['process_data'] == [1.2]

def test_timers_disallow_setitem():
    timers = Timers()
    with pytest.raises(TypeError):
        timers['example'] = 10.5

def test_timers_total():
    timers = Timers()
    timers._timings['load_data'].extend([0.5, 0.3])
    assert timers.total('load_data') == 0.8

def test_timers_mean():
    timers = Timers()
    timers._timings['process_data'].append(1.2)
    assert timers.mean('process_data') == 1.2
    timers._timings['process_data'].append(1.5)
    assert timers.mean('process_data') == pytest.approx(1.35)

def test_timers_count():
    timers = Timers()
    timers._timings['load_data'].extend([0.5, 0.3])
    assert timers.count('load_data') == 2

def test_timers_min_max():
    timers = Timers()
    timers._timings['load_data'].extend([0.5, 0.3, 1.0])
    assert timers.min('load_data') == 0.3
    assert timers.max('load_data') == 1.0

def test_timers_stdev():
    timers = Timers()
    timers._timings['load_data'].append(0.5)
    assert math.isnan(timers.stdev('load_data'))
    timers._timings['load_data'].append(0.3)
    assert timers.stdev('load_data') == pytest.approx(0.14142135623730951)

def test_timers_clear():
    timers = Timers()
    timers._timings['load_data'].extend([0.5, 0.3])
    timers.clear()
    assert list(timers._timings.keys()) == []
