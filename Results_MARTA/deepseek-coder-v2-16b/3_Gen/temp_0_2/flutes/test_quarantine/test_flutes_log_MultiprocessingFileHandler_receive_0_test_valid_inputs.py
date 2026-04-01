
import pytest
from multiprocessing_logging_handler import MultiprocessingFileHandler
import logging
import threading
import queue
import os
import sys
import time

@pytest.fixture(scope="module")
def setup_logger():
    log_path = "test_logfile.log"
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield handler, logger
    os.remove(log_path)  # Clean up the log file after the test

def test_valid_inputs(setup_logger):
    handler, logger = setup_logger
    
    # Test logging a message
    logger.info("This is a test log message.")
    
    # Check if the message was logged correctly by reading the file
    with open(handler._path, 'r') as f:
        logs = f.readlines()
    
    assert len(logs) == 1, "Expected one log entry but found multiple."
    assert "This is a test log message." in logs[0], "Log message does not match expected content."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_inputs.py:3:0: E0401: Unable to import 'multiprocessing_logging_handler' (import-error)


"""