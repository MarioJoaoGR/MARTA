
import pytest
from codetiming._timers import Timers
import collections

# Test initialization with default arguments
def test_init_default():
    timers = Timers()
    assert isinstance(timers, Timers)
    assert hasattr(timers, '_timings')
    assert isinstance(timers._timings, collections.defaultdict)