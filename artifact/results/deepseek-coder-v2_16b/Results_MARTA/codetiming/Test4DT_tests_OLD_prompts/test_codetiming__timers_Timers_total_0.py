
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

# Test scenario 1: test_valid_total_time
def test_valid_total_time():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    assert timers.total('example_timer') == 6.0

# Test scenario 2: test_error_total_time
def test_error_total_time():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    with pytest.raises(KeyError):
        timers.total('nonexistent_timer')

# Test scenario 3: test_error_apply_function
def test_error_apply_function():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), 'nonexistent_timer')
