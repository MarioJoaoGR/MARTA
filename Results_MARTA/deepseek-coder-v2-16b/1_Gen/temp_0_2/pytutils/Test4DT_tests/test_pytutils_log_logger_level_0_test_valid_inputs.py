
import logging
import pytest
from pytutils.log import logger_level

def test_valid_inputs():
    log = logging.getLogger(__name__)
    initial_level = log.level
    
    # Set the logger level to DEBUG within a context block
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
        log.debug('This is a debug message.')  # This should be logged because DEBUG >= DEBUG
        log.info('This is an info message.')    # This won't be logged because INFO < DEBUG
    
    # The logger level should be reset to its original value after the context block
    assert log.level == initial_level
