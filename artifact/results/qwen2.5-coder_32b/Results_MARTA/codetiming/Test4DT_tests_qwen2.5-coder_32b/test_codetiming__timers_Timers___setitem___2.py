
import pytest
from codetiming._timers import Timers
import statistics
import math

def test_setitem_with_valid_float_value():
    timers = Timers()
    with pytest.raises(TypeError):
        timers['boundary_value'] = 2.2250738585072014e-308

def test_add_with_valid_float_value():
    timers = Timers()
    timers.add('boundary_value', 2.2250738585072014e-308)
    assert timers._timings['boundary_value'] == [2.2250738585072014e-308]


def test_stdev_with_single_value():
    timers = Timers()
    timers.add('example_timer', 1.2)
    assert math.isnan(timers.stdev('example_timer'))

def test_stdev_with_empty_list():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('example_timer')

def test_count_with_valid_input():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    assert timers.count('example_timer') == 2


def test_total_with_valid_input():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    assert timers.total('example_timer') == pytest.approx(4.6)


def test_min_with_valid_input():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    assert timers.min('example_timer') == pytest.approx(1.2)


def test_max_with_valid_input():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    assert timers.max('example_timer') == pytest.approx(3.4)


def test_mean_with_valid_input():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    assert timers.mean('example_timer') == pytest.approx(2.3)


def test_median_with_valid_input_odd_count():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    timers.add('example_timer', 5.6)
    assert timers.median('example_timer') == pytest.approx(3.4)

def test_median_with_valid_input_even_count():
    timers = Timers()
    timers.add('example_timer', 1.2)
    timers.add('example_timer', 3.4)
    assert timers.median('example_timer') == pytest.approx(2.3)
