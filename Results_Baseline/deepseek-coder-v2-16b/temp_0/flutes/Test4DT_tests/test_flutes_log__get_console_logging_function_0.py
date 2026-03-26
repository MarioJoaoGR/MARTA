
# Module: flutes.log
from flutes.log import _get_console_logging_function

# Test cases for _get_console_logging_function
def test_get_console_logging_function():
    # Assuming _CONSOLE_LOG_FN is a mock callable object for testing purposes
    from unittest.mock import Mock
    
    # Create a mock console logging function
    mock_log_fn = Mock()
    
    # Set the mock log function as _CONSOLE_LOG_FN for testing
    global _CONSOLE_LOG_FN
    _CONSOLE_LOG_FN = mock_log_fn  # Corrected indentation and syntax here
    
    # Call the function and check if it returns the correct mock log function
    result = _get_console_logging_function()
    assert callable(result), f"Expected a callable, but got {type(result).__name__}"
