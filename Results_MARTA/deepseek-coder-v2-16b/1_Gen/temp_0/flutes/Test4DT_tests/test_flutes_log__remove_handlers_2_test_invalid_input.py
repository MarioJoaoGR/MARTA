
import logging
import os
import pytest
from unittest.mock import patch

# Assuming _remove_handlers is defined in your module
def _remove_handlers(logger):
    while len(logger.handlers) > 0:
        handler = logger.handlers[0]
        handler.close()
        logger.removeHandler(handler)

@pytest.mark.parametrize("invalid_logger", [None, "invalid_type"])
def test_invalid_input(invalid_logger):
    with patch.dict(os.environ, {"LOGGING_LOGGER": "some_valid_logger"}):
        logger = logging.getLogger('some_valid_logger')
        
        # Set up a mock handler to simulate having handlers in the logger
        mock_handler = logging.Handler()
        logger.addHandler(mock_handler)
        
        with pytest.raises(AttributeError):
            _remove_handlers(invalid_logger if isinstance(invalid_logger, str) else invalid_logger.__class__)
