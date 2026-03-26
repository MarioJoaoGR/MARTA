
import pytest
from pytutils.timers import Timer
import time

def test_valid_inputs():
    # Define a mock function to be timed
    def mock_function():
        time.sleep(1)  # Sleep for 1 second to simulate work
    
    with Timer(name="test_block", verbose=True) as t:
        mock_function()  # The mock function should take approximately 1 second to execute
        
    # Check that the output is captured and can be verified or further processed if necessary
    # For this simple example, we assume the timer prints the elapsed time directly in a readable format.
    assert t.name == "test_block"
    assert t.verbose is True
