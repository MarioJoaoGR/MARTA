
import pytest
from flutes.log import MultiprocessingFileHandler
import logging
import multiprocessing
import threading
import time
import os

@pytest.fixture(scope="module")
def setup_logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    
    # Create a handler for the logger
    log_path = "test_logfile.log"
    handler = MultiprocessingFileHandler(log_path, mode="a")
    
    # Add the handler to the logger
    logger.addHandler(handler)
    
    yield (logger, handler)
    
    # Teardown: Remove the log file if it exists
    if os.path.exists(log_path):
        os.remove(log_path)

def test_multiprocessing_log_handler(setup_logger):
    logger, handler = setup_logger
    
    # Log a message
    logger.info("Test log message")
    
    # Wait for the logging thread to write the message to the file
    time.sleep(1)  # Adjust sleep time if necessary
    
    # Check that the log file has been written to correctly
    with open(handler._path, "r") as f:
        content = f.read()
        assert "Test log message" in content, "Log message not found in log file."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_______________________ test_multiprocessing_log_handler _______________________

setup_logger = (<Logger test_logger (DEBUG)>, <MultiprocessingFileHandler (NOTSET)>)

    def test_multiprocessing_log_handler(setup_logger):
        logger, handler = setup_logger
    
        # Log a message
        logger.info("Test log message")
    
        # Wait for the logging thread to write the message to the file
        time.sleep(1)  # Adjust sleep time if necessary
    
        # Check that the log file has been written to correctly
>       with open(handler._path, "r") as f:
E       AttributeError: 'MultiprocessingFileHandler' object has no attribute '_path'

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_edge_case.py:38: AttributeError
------------------------------ Captured log call -------------------------------
INFO     test_logger:test_flutes_log_MultiprocessingFileHandler_receive_0_test_edge_case.py:32 Test log message
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_edge_case.py::test_multiprocessing_log_handler
============================== 1 failed in 1.10s ===============================
"""