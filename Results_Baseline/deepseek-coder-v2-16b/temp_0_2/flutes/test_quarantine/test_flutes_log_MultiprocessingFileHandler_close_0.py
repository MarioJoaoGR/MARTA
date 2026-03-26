
# Module: flutes.log
import pytest
from pathlib import Path
import logging
import multiprocessing
import threading
import queue
import multiprocessing_log_handler as mplh

# Fixture to create a temporary log file for testing
@pytest.fixture(scope="module")
def temp_log_file():
    # Create a temporary log file path
    log_file = Path("logs/test_app.log")
    yield log_file  # Provide the fixture value
    if log_file.exists():
        log_file.unlink()  # Remove the log file after the test

# Test initialization with default mode
def test_init_default_mode(temp_log_file):
    handler = mplh.MultiprocessingFileHandler(temp_log_file)
    assert isinstance(handler._handler, logging.FileHandler), "Expected _handler to be a FileHandler instance"
    assert isinstance(handler.queue, multiprocessing.Queue), "Expected queue to be a multiprocessing Queue"
    assert handler._handler.mode == 'a', "Expected mode to be append ('a')"

# Test initialization with specified mode
def test_init_specified_mode(temp_log_file):
    handler = mplh.MultiprocessingFileHandler(temp_log_file, mode="w")
    assert isinstance(handler._handler, logging.FileHandler), "Expected _handler to be a FileHandler instance"
    assert isinstance(handler.queue, multiprocessing.Queue), "Expected queue to be a multiprocessing Queue"
    assert handler._handler.mode == 'w', "Expected mode to be write ('w')"

# Test logging message
def test_logging_message(temp_log_file):
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    handler = mplh.MultiprocessingFileHandler(temp_log_file)
    logger.addHandler(handler)
    logger.info('This is an info message')
    
    # Check if the log file contains the expected message
    with open(temp_log_file, 'r') as f:
        logs = f.readlines()
    assert "This is an info message" in logs[-1], "Expected log to contain the info message"

# Test logging from multiple processes
def test_logging_from_multiple_processes():
    def worker(queue):
        logger = logging.getLogger('my_logger')
        handler = mplh.MultiprocessingFileHandler(Path("logs/test_app.log"))
        queue.put(handler)  # Put the handler into the queue for other processes to use
        logger.addHandler(handler)
        logger.info('This is an info message from a worker process')

    if __name__ == '__main__':
        queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=worker, args=(queue,))
        p.start()
        p.join()  # Wait for the worker to finish
        
        with open("logs/test_app.log", 'r') as f:
            logs = f.readlines()
        assert "This is an info message from a worker process" in logs[-1], "Expected log to contain the multi-process info message"

# Test closing the handler
def test_close(temp_log_file):
    handler = mplh.MultiprocessingFileHandler(temp_log_file)
    assert not temp_log_file.exists(), "Log file should exist before closing"
    handler.close()
    assert not handler._handler.stream.closed, "Stream should be closed after close method is called"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_close_0
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_close_0.py:9:0: E0401: Unable to import 'multiprocessing_log_handler' (import-error)


"""