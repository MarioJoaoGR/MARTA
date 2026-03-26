
import pytest
from pytutils.log import logger_level
import logging

def test_logger_level():
    log = logging.getLogger(__name__)
    
    # Save the initial level
    initial_level = log.level
    
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
        log.debug('This is a debug message.')  # This will be logged because the level is set to DEBUG
        log.info('This is an info message.')    # This won't be logged because INFO >= DEBUG
    
    # Check if the logger level reverts back to its original setting after the context block
    assert log.level == initial_level
    log.error('This is an error message.')  # This will be logged as it was before the context block
