
import pytest
from codetiming._timers import Timers
import collections
import statistics
from typing import List, Callable, Any, Dict, TypeVar

T = TypeVar('T')

def test_init():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert isinstance(timers._timings, dict)
    assert len(timers._timings) == 0

def test_apply_keyerror():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "example_timer")

def test_median_no_values():
    timers = Timers()