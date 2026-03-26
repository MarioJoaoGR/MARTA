
import pytest
from codetiming import Timer
from codetiming._timer import Timers

def test_valid_inputs():
    timer = Timer()
    assert isinstance(timer.timers, Timers), f"Expected timers to be an instance of Timers but got {type(timer.timers)}"
