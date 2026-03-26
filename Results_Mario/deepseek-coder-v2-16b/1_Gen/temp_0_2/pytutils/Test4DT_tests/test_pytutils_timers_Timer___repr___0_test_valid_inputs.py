
import pytest
from pytutils.timers import Timer

def test_valid_inputs():
    # Test case 1: Default parameters
    with Timer() as t:
        pass  # No operation, just timing
    
    # Test case 2: With name and verbose enabled
    with Timer('operation', verbose=True) as t:
        pass  # No operation, just timing
    
    # Test case 3: With name and verbose disabled
    with Timer('operation') as t:
        pass  # No operation, just timing
