
import pytest
from semantic_release.helpers import LoggedFunction
import logging

# Set up a logger for testing
logger = logging.getLogger("test_logger")
logged_function = LoggedFunction(logger)

@logged_function
def example_function(a, b):
    """Example function to be decorated with debug logging."""
    return a + b

# Test the LoggedFunction decorator
def test_logged_function():
    # Call the decorated function
    result = example_function(3, 4)
    
    # Assert that the result is correct
    assert result == 7
