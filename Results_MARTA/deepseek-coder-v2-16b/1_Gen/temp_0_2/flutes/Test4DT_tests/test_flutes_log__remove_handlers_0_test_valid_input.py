
import pytest
from unittest.mock import MagicMock
import logging

# Assuming the module 'flutes.log' has a function _remove_handlers defined as shown in the provided code
def _remove_handlers(logger):
    while len(logger.handlers) > 0:
        handler = logger.handlers[0]
        handler.close()
        logger.removeHandler(handler)

# Test case for valid input scenario
def test_valid_input():
    # Create a mock logger
    logger = logging.getLogger('my_logger')
    logger.handlers = [MagicMock(), MagicMock()]  # Add some mock handlers to the logger
    
    # Call the function under test
    _remove_handlers(logger)
    
    # Assert that all handlers have been removed
    assert len(logger.handlers) == 0
