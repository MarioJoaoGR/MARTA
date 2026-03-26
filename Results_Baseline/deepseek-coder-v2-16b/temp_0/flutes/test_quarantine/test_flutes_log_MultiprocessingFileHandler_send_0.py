
# Module: flutes.log
import pytest
import logging
import multiprocessing as mp
from pathlib import Path
from your_module import MultiprocessingFileHandler  # Replace 'your_module' with the actual module name where the handler is defined

# Fixture to create a logger and handler for testing
@pytest.fixture(scope="function")
def setup_logger():
    log_path = Path("logs/test.log")
    handler = MultiprocessingFileHandler(log_path)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    yield logger, handler
    
    # Teardown: Remove the handler and close the queue
    for h in logger.handlers:
        logger.removeHandler(h)
    handler.queue.put_nowait("CLOSE")  # Signal to stop the thread
    handler.queue.close()
    handler.queue.join_thread()

def test_send_log_message(setup_logger):
    logger, handler = setup_logger
    
    # Test sending a log message
    log_message = "Test log message"
    handler.send(log_message)
    
    # Retrieve the log message from the queue and assert it is in the log file
    with open("logs/test.log", "r") as f:
        logs = f.readlines()
        assert len(logs) == 1, "Expected one log message but found more or none."
        assert log_message in logs[0], "Log message not found in the log file."

def test_multiple_send_log_messages(setup_logger):
    logger, handler = setup_logger
    
    # Test sending multiple log messages
    log_messages = ["Log message 1", "Log message 2", "Log message 3"]
    for msg in log_messages:
        handler.send(msg)
    
    # Retrieve the log messages from the queue and assert they are in the log file
    with open("logs/test.log", "r") as f:
        logs = f.readlines()
        for msg in log_messages:
            assert msg in logs, f"Log message '{msg}' not found in the log file."

def test_send_and_close(setup_logger):
    logger, handler = setup_logger
    
    # Test sending a log message and then closing the queue
    log_message = "Test close log message"
    handler.send(log_message)
    handler.send("CLOSE")  # Signal to stop the thread
    
    # Retrieve the log messages from the queue and assert they are in the log file
    with open("logs/test.log", "r") as f:
        logs = f.readlines()
        assert len(logs) == 1, "Expected one log message but found more or none."
        assert log_message in logs[0], "Log message not found in the log file."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_send_0
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0.py:7:0: E0401: Unable to import 'your_module' (import-error)


"""