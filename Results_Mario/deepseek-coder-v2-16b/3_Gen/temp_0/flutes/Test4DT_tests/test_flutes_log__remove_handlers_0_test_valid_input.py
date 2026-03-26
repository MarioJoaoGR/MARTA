
import logging
import pytest
from unittest.mock import MagicMock

# Assuming _remove_handlers is defined in your module or script
def _remove_handlers(logger):
    while len(logger.handlers) > 0:
        handler = logger.handlers[0]
        handler.close()
        logger.removeHandler(handler)

@pytest.fixture
def setup_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    # Add two handlers for the test
    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler('test.log')
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    
    yield logger
    
    # Teardown: Remove all handlers after the test
    _remove_handlers(logger)

def test_valid_input(setup_logger):
    logger = setup_logger
    assert len(logger.handlers) == 2
    
    # Call the function to remove handlers
    _remove_handlers(logger)
    
    # Check that all handlers have been removed
    assert len(logger.handlers) == 0
