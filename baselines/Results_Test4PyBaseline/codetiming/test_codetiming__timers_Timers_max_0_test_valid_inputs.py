
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_valid_inputs():
    timers = Timers()
    
    # Add some timing data to the timers instance
    timers._timings['test_timer'].extend([1.0, 2.0, 3.0])
    
    assert timers.max('test_timer') == 3.0
