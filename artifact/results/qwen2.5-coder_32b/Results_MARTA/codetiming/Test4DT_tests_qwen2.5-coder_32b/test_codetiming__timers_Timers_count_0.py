
import pytest
from codetiming._timers import Timers

def test_count_with_valid_input():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert timers.count('example_timer') == 3

def test_count_with_empty_list():
    timers = Timers()
    timers._timings['example_timer'] = []
    assert timers.count('example_timer') == 0

def test_count_with_missing_key():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.count('missing_timer')
