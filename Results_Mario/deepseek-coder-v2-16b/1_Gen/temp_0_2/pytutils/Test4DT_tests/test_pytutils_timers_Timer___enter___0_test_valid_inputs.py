
import pytest
from pytutils.timers import Timer
import time

def test_valid_inputs():
    # Test without name and verbose=True
    with Timer(verbose=True) as t:
        time.sleep(0.1)  # This should take more than 0 seconds but less than 0.1 seconds
    assert hasattr(t, 'start')
    assert hasattr(t, 'name')
    assert t.name == ''
    assert isinstance(t.verbose, bool)
    assert isinstance(t.start, float)
    
    # Test with name and verbose=False
    with Timer(name='test_timer', verbose=False) as t:
        time.sleep(0.1)  # This should take more than 0 seconds but less than 0.1 seconds
    assert hasattr(t, 'start')
    assert hasattr(t, 'name')
    assert t.name == 'test_timer'
    assert isinstance(t.verbose, bool)
    assert isinstance(t.start, float)
