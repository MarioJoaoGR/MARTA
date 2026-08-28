
import pytest
import logging
from pytutils.log import get_logger

# Ensure the logging system is configured before running tests
logging.basicConfig()

def test_default_logger():
    log = get_logger()
    assert isinstance(log, logging.Logger)
    log.info('test')
    # Assuming a logger with name 'root' should have at least the root level set by default