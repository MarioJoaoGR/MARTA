
import pytest
import logging
from unittest.mock import patch
from pytutils.log import get_logger, _ensure_configured, _namespace_from_calling_context

# Test case for valid input (default name)
def test_valid_input_default():
    with patch('pytutils.log._ensure_configured'):
        log = get_logger()
        assert isinstance(log, logging.Logger), "Expected a logger instance"
        log.info("Test message")

# Test case for valid input (custom name)
def test_valid_input_custom():
    with patch('pytutils.log._ensure_configured'):
        log = get_logger('custom')
        assert isinstance(log, logging.Logger), "Expected a logger instance"
        log.info("Test message")

# Test case for invalid input (None)