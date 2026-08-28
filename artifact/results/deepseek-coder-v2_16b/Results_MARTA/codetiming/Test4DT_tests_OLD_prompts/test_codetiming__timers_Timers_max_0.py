
import pytest
from unittest.mock import patch, MagicMock
from codetiming._timers import Timers

# Test for invalid input where the timings dictionary contains None values

# Test for no values in the timings dictionary

# Test for valid input where timings dictionary contains values
def test_valid_input():
    timers = Timers()
    timers._timings['valid_task'] = [1.0, 2.0, 3.0]
    assert timers.max('valid_task') == 3.0