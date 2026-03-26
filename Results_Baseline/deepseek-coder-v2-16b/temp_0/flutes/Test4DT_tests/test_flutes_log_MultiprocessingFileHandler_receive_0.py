
import pytest
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler  # Replace 'flutes.log' with the actual module name where the handler is defined
import threading
import traceback
import sys

# Helper function to create a temporary log file for testing
def setup_logger():
    log_path = Path("test.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return log_path, handler, logger

# Test case for the initialization of MultiprocessingFileHandler
def test_multiprocessingfilehandler_init():
    log_path = Path("test.log")
    handler = MultiprocessingFileHandler(log_path)
    assert isinstance(handler._handler, logging.FileHandler), "Expected _handler to be an instance of logging.FileHandler"