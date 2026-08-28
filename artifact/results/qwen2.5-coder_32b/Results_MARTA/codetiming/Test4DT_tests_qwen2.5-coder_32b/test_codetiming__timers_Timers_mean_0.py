
import pytest
from codetiming._timers import Timers
import statistics

def test_mean_happy_path():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert timers.mean('example_timer') == statistics.mean([1.2, 3.4, 5.6])

def test_mean_edge_cases():
    timers = Timers()
    timers._timings['empty_timer'] = []
    timers._timings['boundary_timer'] = [0.0, 100.0]
    
    assert timers.mean('empty_timer') == 0.0
    assert timers.mean('boundary_timer') == statistics.mean([0.0, 100.0])

def test_mean_invalid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.mean('non_existent_key')
