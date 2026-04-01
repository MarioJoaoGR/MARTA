
import pytest
from flutes.log import _remove_handlers
import logging

def test_valid_input():
    # Create a logger instance
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    # Add some handlers to the logger (this is just an example, in practice you might have already added handlers)
    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler('example.log')
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    
    # Ensure there are two handlers before removal
    assert len(logger.handlers) == 2
    
    # Remove all handlers from the logger
    _remove_handlers(logger)
    
    # Ensure that no handlers are left after removal
    assert len(logger.handlers) == 0
