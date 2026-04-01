
import logging
import pytest
from pytutils.log import logger_level

def test_valid_inputs():
    log = logging.getLogger(__name__)
    initial_level = log.level
    
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
        log.debug('This is a debug message.')
        log.info('This is an info message.')  # This should not be logged
        
    assert log.level == initial_level
    log.error('This is an error message.')  # This should be logged as it was before the context block
