
import pytest
from unittest.mock import MagicMock
import logging

# Assuming the module is named 'flutes.log'
from flutes.log import _remove_handlers

def test_invalid_input():
    # Create a logger with no handlers
    logger = logging.getLogger('my_logger')
    
    # Ensure there are no handlers initially
    assert len(logger.handlers) == 0
    
    # Mock the close method of a handler to simulate closing
    mock_handler1 = MagicMock()
    mock_handler2 = MagicMock()
    
    # Add some handlers to the logger (mocked)
    logger.addHandler(mock_handler1)
    logger.addHandler(mock_handler2)
    
    # Ensure there are now two handlers in the logger
    assert len(logger.handlers) == 2
    
    # Call the function to remove all handlers
    _remove_handlers(logger)
    
    # Ensure no handlers are left after calling the function
    assert len(logger.handlers) == 0
    
    # Verify that the close method was called for both handlers
    mock_handler1.close.assert_called_once()
    mock_handler2.close.assert_called_once()
