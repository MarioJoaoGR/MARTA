
import pytest
from codetiming._timers import Timers

def test_edge_cases():
    timers = Timers()
    assert isinstance(timers._timings, dict)
    assert len(timers._timings) == 0
