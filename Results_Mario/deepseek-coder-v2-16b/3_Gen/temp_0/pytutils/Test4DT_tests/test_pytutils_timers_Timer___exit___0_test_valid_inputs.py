
import pytest
from pytutils.timers import Timer
import time

def test_valid_inputs():
    # Test case where verbose is True and name is provided
    with Timer(name='test_operation', verbose=True) as t:
        time.sleep(1)  # This should take approximately 1 second
    
    assert hasattr(t, 'secs')
    assert hasattr(t, 'msecs')
