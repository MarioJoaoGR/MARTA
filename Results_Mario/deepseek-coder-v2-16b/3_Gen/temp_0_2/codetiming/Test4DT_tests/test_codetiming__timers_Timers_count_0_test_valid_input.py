
import pytest
from codetiming._timers import Timers

def test_valid_input():
    timers = Timers()
    timers._timings["test_timer"].append(1.0)
    assert timers.count("test_timer") == 1.0
