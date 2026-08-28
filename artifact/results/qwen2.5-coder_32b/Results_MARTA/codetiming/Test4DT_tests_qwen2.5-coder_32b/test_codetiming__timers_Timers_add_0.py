
import pytest
from codetiming._timers import Timers




def test_valid_addition():
    timers = Timers()
    timers.add('valid_case', 1.5)
    assert timers.data['valid_case'] == 1.5  # Ensure the value is added correctly

def test_multiple_additions():
    timers = Timers()
    timers.add('multiple_case', 1.0)
    timers.add('multiple_case', 2.0)
    assert timers.data['multiple_case'] == 3.0  # Ensure values are summed correctly

def test_initialization_no_data():
    timers = Timers()
    assert not timers.data  # Ensure data is empty on initialization