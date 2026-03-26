
import pytest
from codetiming._timers import Timers
import collections
from typing import List, Callable, Dict, Any

# Test initialization of Timers class
def test_init():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert timers._timings == collections.defaultdict(list)

# Test apply method with existing timer name
def test_apply_existing_timer():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    result = timers.apply(lambda x: sum(x), "example_timer")