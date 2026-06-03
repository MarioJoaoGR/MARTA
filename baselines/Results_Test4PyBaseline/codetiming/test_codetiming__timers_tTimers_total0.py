# Module: codetiming._timers
import pytest
from collections import defaultdict
from typing import Any, Callable, Dict, List
import codetiming._timers as ct_timers

# Test initialization of Timers class
def test_timers_init():
    timers = ct_timers.Timers()
    assert isinstance(timers._timings, defaultdict)
    assert isinstance(timers._timings['default'], list)

# Test apply method with valid input
def test_apply_valid():
    timers = ct_timers.Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    result = timers.apply(lambda x: sum(x), 'example_timer')
    assert result == 6.0

# Test apply method with invalid input (KeyError expected)
def test_apply_invalid():
    timers = ct_timers.Timers()
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), 'nonexistent_timer')

# Test total method with valid input
def test_total_valid():
    timers = ct_timers.Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    assert timers.total('example_timer') == 6.0

# Test total method with invalid input (KeyError expected)
def test_total_invalid():
    timers = ct_timers.Timers()
    with pytest.raises(KeyError):
        timers.total('nonexistent_timer')
