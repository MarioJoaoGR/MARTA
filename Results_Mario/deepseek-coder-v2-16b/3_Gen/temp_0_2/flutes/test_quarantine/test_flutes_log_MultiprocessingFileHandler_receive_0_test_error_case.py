
import pytest
from flutes.log import MultiprocessingFileHandler
import multiprocessing
import logging
import threading
import queue
import sys
import traceback

@pytest.fixture(scope="module")
def setup_logger():
    log_path = "test_logfile.log"
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield handler, logger
    # Clean up the log file after the test
    with open(log_path, 'w') as f:
        f.truncate(0)

def test_receive(setup_logger):
    handler, logger = setup_logger
    
    # Create a logging record
    record = logging.LogRecord('test_module', logging.DEBUG, __file__, 10, 'Test message', (), None)
    
    # Put the record in the queue
    handler.queue.put(record)
    
    # Give some time for the receive method to process the record
    threading.Event().wait(0.1)
    
    # Check if the log file contains the test message
    with open(log_path, 'r') as f:
        content = f.read()
        assert "Test message" in content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_receive_0_test_error_case
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_error_case.py:36:14: E0602: Undefined variable 'log_path' (undefined-variable)


"""