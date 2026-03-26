
import pytest
from codetiming._timers import Timers
import collections

def test_edge_case():
    timers = Timers()
    
    # Test with None value
    with pytest.raises(KeyError):
        assert timers.min("test_timer") is 0
    
    # Add a timing for the given name
    timers._timings["test_timer"].append(10.0)
    
    # Test with valid timing
    assert timers.min("test_timer") == 10.0
    
    # Test with empty list
    timers._timings["empty_list_timer"] = []
    assert timers.min("empty_list_timer") == 0
    
    # Add another timing for a different name
    timers._timings["another_timer"].append(20.0)
    
    # Test with multiple timings
    assert timers.min("another_timer") == 20.0
