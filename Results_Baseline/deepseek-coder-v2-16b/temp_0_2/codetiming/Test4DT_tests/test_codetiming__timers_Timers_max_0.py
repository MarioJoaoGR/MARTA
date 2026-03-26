
import pytest
from codetiming._timers import Timers
import time

# Test initialization of Timers class
def test_init():
    timers = Timers()
    assert isinstance(timers, Timers), "Timers instance should be an instance of Timers"
    assert hasattr(timers, '_timings'), "_timings attribute not found in Timers instance"