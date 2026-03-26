
import pytest
from flutes.log import MultiprocessingFileHandler
import logging
import multiprocessing
import threading

@pytest.fixture(scope="module")
def setup_logger():
    logger = logging.getLogger("test_logger")
    handler = MultiprocessingFileHandler('logs/test.log')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger, handler

def test_valid_input(setup_logger):
    logger, handler = setup_logger
    
    # Log a message to trigger the multiprocessing logging mechanism
    logger.info('Test log message')
    
    # Ensure that the queue is used and messages are processed by the handler
    assert handler.queue.qsize() > 0
