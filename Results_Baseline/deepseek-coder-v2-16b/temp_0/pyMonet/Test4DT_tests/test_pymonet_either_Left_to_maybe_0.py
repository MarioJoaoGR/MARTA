# Module: pymonet.either
# Importing the Left class if not already imported
from pymonet.either import Left
import pytest

# Test case for to_maybe method when called on an instance of Left
def test_to_maybe_left():
    # Creating an instance of Left with a value representing failure or no result
    left_instance = Left("error message")  # Create an instance of Left
    
    # Calling the to_maybe method on the Left instance
    maybe_instance = left_instance.to_maybe()  # Convert it to a Maybe type
    
    # Checking if the Maybe represents nothing (no value)
    assert maybe_instance.is_nothing, "Expected is_nothing to be True"
