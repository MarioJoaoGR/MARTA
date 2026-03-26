
import pytest
from codetiming import Timer
import time
import math

def test_valid_inputs():
    timer = Timer(text='Elapsed time: {:0.4f} seconds')
    
    with timer as t:
        # Simulate some code execution time
        time.sleep(0.1)
        
    assert isinstance(t, Timer), "The context manager should return an instance of Timer"
    assert math.isnan(timer.last) == False, "The last attribute should be updated with the elapsed time after exiting the context manager"
