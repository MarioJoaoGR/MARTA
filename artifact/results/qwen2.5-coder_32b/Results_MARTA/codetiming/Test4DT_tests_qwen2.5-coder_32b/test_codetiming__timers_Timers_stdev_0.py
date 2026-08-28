
import pytest
from codetiming._timers import Timers
import math
import statistics

def test_empty_list():
    timers = Timers()
    timers._timings['empty'] = []
    assert math.isnan(timers.stdev('empty'))

def test_single_element_list():
    timers = Timers()
    timers._timings['single'] = [1.0]
    assert math.isnan(timers.stdev('single'))

def test_two_elements_list():
    timers = Timers()
    timers._timings['two_elements'] = [1.0, 2.0]
    expected_stdev = statistics.stdev([1.0, 2.0])
    assert timers.stdev('two_elements') == pytest.approx(expected_stdev)

def test_multiple_elements_list():
    timers = Timers()
    timers._timings['multiple'] = [1.0, 2.0, 3.0, 4.0]
    expected_stdev = statistics.stdev([1.0, 2.0, 3.0, 4.0])
    assert timers.stdev('multiple') == pytest.approx(expected_stdev)

def test_non_existent_key():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('non_existent')
