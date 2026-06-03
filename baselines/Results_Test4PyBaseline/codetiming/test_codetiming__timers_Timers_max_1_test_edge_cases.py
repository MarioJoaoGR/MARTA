
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_edge_cases():
    timers = Timers()
    
    # Test with None as input
    with pytest.raises(KeyError):
        assert timers.max(None) is None
    
    # Test with empty list
    timers._timings['test'] = []
    assert timers.max('test') == 0
    
    # Test with single value in the list
    timers._timings['test'].append(1.0)
    assert timers.max('test') == 1.0
    
    # Test with multiple values in the list
    timers._timings['test'].extend([2.0, 3.0, 4.0])
    assert timers.max('test') == 4.0
