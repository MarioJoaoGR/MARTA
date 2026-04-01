
import logging
import pytest
from pytutils.log import get_logger

def test_valid_input():
    # Test without providing a name
    log = get_logger()
    assert isinstance(log, logging.Logger), "Expected a logger instance"
    log.info('test')  # Check if the info message is logged correctly
    
    # Test with providing a specific name
    log = get_logger('test2')
    assert isinstance(log, logging.Logger), "Expected a logger instance"
    log.info('test2')  # Check if the info message is logged correctly
