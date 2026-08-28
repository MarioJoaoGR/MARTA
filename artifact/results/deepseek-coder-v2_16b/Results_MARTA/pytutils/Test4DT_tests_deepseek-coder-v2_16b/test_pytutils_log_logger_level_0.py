
import pytest
import logging
from pytutils.log import logger_level

def test_valid_logger_level():
    log = logging.getLogger(__name__)
    initial_level = log.level
    
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
    
    assert log.level == initial_level
