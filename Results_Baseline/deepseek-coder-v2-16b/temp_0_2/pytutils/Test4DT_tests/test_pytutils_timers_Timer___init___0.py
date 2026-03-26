
import pytest
from pytutils.timers import Timer
import time

# Test cases for Timer class
def test_timer_basic():
    with Timer('long_operation', verbose=True) as t:
        time.sleep(2)  # Example of a long operation
    assert hasattr(t, 'name') and t.name == 'long_operation'
    assert hasattr(t, 'verbose') and t.verbose is True

def test_timer_default_name():
    with Timer() as t:
        time.sleep(2)  # Example of a long operation