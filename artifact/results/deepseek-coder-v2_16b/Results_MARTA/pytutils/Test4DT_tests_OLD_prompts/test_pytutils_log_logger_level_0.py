
import pytest
import logging
from pytutils.log import logger_level

def test_logger_level_context():
    log = logging.getLogger(__name__)
    
    # Ensure the initial level is not DEBUG
    assert log.level != logging.DEBUG, "Initial logger level should not be DEBUG"
    
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG, "Logger level should be set to DEBUG within the context block"
    
    # Ensure the level reverts back after the context block
    assert log.level != logging.DEBUG, "Logger level should revert back to its original state after the context block"
