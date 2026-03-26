
import pytest
from codetiming._timers import Timers
import collections
import statistics
from typing import List, Callable, Any, Dict, TypeVar

T = TypeVar('T')

def test_median_no_values():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median("example_timer")

def test_median_single_value():
    timers = Timers()
    timers._timings["example_timer"] = [10]
    assert timers.median("example_timer") == 10

def test_median_multiple_values():
    timers = Timers()
    timers._timings["example_timer"] = [5, 10, 15]
    assert timers.median("example_timer") == 10

def test_median_even_number_of_values():
    timers = Timers()
    timers._timings["example_timer"] = [4, 6, 8, 10]
    assert timers.median("example_timer") == (6 + 8) / 2

def test_median_odd_number_of_values():
    timers = Timers()
    timers._timings["example_timer"] = [3, 6, 7, 8, 9]
    assert timers.median("example_timer") == 7

def test_median_zero_values():
    timers = Timers()
    timers._timings["example_timer"] = []
    assert timers.median("example_timer") == 0
