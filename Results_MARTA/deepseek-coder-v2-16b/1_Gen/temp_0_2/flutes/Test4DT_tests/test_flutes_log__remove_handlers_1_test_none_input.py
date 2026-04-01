
import logging
from unittest.mock import MagicMock
import pytest

def test_none_input():
    # Create a mock logger
    logger = logging.getLogger('my_logger')
    logger.handlers = []  # Initialize an empty list of handlers for the mock logger

    # Call the function with the mock logger
    from flutes.log import _remove_handlers
    _remove_handlers(logger)

    # Check that no handlers are left in the logger after calling the function
    assert len(logger.handlers) == 0, "Expected no handlers to be present after removal."
