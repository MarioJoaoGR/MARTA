
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

# Test valid input scenario
def test_valid_input():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    assert timers.min('example_timer') == 1.0

# Test edge case scenario with empty list and no timings
def test_edge_case():
    timers = Timers()
    timers._timings['empty'] = []
    assert timers.min('empty') == 0

# Test raising KeyError for non-existent timer
def test_invalid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.min('non_existent_timer')
