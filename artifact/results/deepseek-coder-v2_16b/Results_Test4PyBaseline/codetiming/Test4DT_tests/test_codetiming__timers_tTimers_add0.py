
import pytest
from codetiming._timers import Timers
import collections

# Test initialization with default arguments
def test_init_default():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert timers._timings == {}