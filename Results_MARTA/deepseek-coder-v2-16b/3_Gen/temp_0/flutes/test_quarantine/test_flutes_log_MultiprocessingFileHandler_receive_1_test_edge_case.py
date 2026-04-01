
import pytest
from pathlib import Path
import multiprocessing
import logging
import sys
import traceback
from unittest.mock import MagicMock, patch

# Assuming the module 'flutes.log' contains the MultiprocessingFileHandler class
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

def test_logger_emits_records_to_file(logger):
    # Create a mock record to simulate log entry
    record = logging.LogRecord(
        name=__name__,
        level=logging.DEBUG,
        pathname="test_path",
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None
    )

    # Use a multiprocessing process to add the record to the queue
    def add_record_to_queue():
        logger.handlers[0].queue.put(record)

    # Start a new process to add the record to the queue
    p = multiprocessing.Process(target=add_record_to_queue)
    p.start()
    p.join()

    # Check if the record was added to the file
    with open("logs/app.log", "r") as log_file:
        logs = log_file.readlines()
        assert len(logs) > 0, "No logs were written to the file"
        assert "Test message" in logs[-1], "The log message was not found in the file"
