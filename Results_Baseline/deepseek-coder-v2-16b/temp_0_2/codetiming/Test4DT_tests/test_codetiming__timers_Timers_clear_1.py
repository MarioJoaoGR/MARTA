
import pytest
from collections import defaultdict
try:
    from codetiming._timers import Timers
except ImportError:
    # If the module is not found, skip the test
    pytest.skip("Module 'codetiming._timers' not found", allow_module_level=True)

def test_clear():
    timers = Timers()
    timers._timings['test'] = [1.0]  # Adding a timing entry for the key 'test'
    timers.data['test'] = "value"   # Corrected to use the correct attribute name
    
    timers.clear()
    
    assert len(timers._timings) == 0, "Timings dictionary should be cleared."
    assert len(timers.data) == 0, "Data dictionary should be cleared."

def test_clear_empty():
    timers = Timers()
    
    timers.clear()
    
    assert len(timers._timings) == 0, "Timings dictionary should remain empty if it was already empty."
    assert len(timers.data) == 0, "Data dictionary should remain empty if it was already empty."

def test_clear_multiple():
    timers = Timers()
    timers._timings['test1'] = [1.0]
    timers.data['test1'] = "value1"
    timers._timings['test2'] = [2.0]
    timers.data['test2'] = "value2"
    
    timers.clear()
    
    assert len(timers._timings) == 0, "Timings dictionary should be cleared."
    assert len(timers.data) == 0, "Data dictionary should be cleared."
