
import pytest
import logging
import threading
import multiprocessing as mp
from pathlib import Path
from unittest.mock import patch

# Import the function from the module
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def logger():
    log = logging.getLogger('my_logger')
    log.setLevel(logging.DEBUG)
    return log

@pytest.fixture(scope="module")
def handler():
    return MultiprocessingFileHandler(Path("logs/app.log"))

def test_basic_initialization(logger, handler):
    logger.addHandler(handler)
    assert isinstance(logger.handlers[0], type(handler))

def test_send_log_message(logger, handler):
    logger.addHandler(handler)
    message = "This is another info message"
    handler.send(message)
    # Assuming the log message gets processed by the thread and written to a file