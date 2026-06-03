
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_valid_input():
    timers = Timers()
    
    # Add some timing data
    timers._timings['test_timer'].append(1.0)
    timers._timings['test_timer'].append(2.0)
    timers._timings['test_timer'].append(3.0)
    
    # Test the total method with valid input
    assert timers.total('test_timer') == 6.0
