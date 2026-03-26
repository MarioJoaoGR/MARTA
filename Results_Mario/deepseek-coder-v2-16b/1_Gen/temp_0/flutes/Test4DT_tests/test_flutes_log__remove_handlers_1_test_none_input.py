
import pytest
from flutes.log import _remove_handlers
import logging

def test_none_input():
    # Create a mock logger with no handlers
    logger = logging.getLogger('test_logger')
    
    # Ensure there are no handlers initially
    assert len(logger.handlers) == 0
    
    # Call the function to remove handlers (which should do nothing since there are none)
    _remove_handlers(logger)
    
    # Verify that after calling the function, there are still no handlers
    assert len(logger.handlers) == 0
