
import logging
import pytest
from pytutils.log import logger_level

def test_valid_inputs():
    log = logging.getLogger(__name__)
    initial_level = log.level
    
    # Test setting the level to DEBUG
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
        log.debug('This is a debug message.')
        log.info('This is an info message.')
        
    # After the context block, the level should revert back to its initial value
    assert log.level == initial_level
    
    # Test setting the level to INFO
    with logger_level(log, logging.INFO):
        assert log.level == logging.INFO
        log.info('This is an info message.')
        log.warning('This is a warning message.')
        
    # After the context block, the level should revert back to its initial value
    assert log.level == initial_level
    
    # Test setting the level to WARNING
    with logger_level(log, logging.WARNING):
        assert log.level == logging.WARNING
        log.warning('This is a warning message.')
        log.error('This is an error message.')
        
    # After the context block, the level should revert back to its initial value
    assert log.level == initial_level
    
    # Test setting the level to ERROR
    with logger_level(log, logging.ERROR):
        assert log.level == logging.ERROR
        log.error('This is an error message.')
        log.critical('This is a critical message.')
        
    # After the context block, the level should revert back to its initial value
    assert log.level == initial_level
