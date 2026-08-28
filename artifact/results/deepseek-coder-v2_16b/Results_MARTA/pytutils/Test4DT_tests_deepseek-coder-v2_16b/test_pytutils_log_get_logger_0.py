
import logging
import pytest
from pytutils.log import get_logger  # Assuming this module exists and contains the get_logger function

# Test for default logger name
def test_valid_input_default_logger():
    log = get_logger()
    assert isinstance(log, logging.Logger)
    log.info('This is a test message.')

# Test for custom logger name
def test_valid_input_custom_logger():
    log = get_logger('custom_logger')
    assert isinstance(log, logging.Logger)
    log.info('This is another test message with a custom logger.')

# Test handling of None input
def test_invalid_input_none():
    log = get_logger(None)
    assert isinstance(log, logging.Logger)
    log.info('Test message with None input')
