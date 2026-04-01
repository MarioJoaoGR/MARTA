
import pytest
import multiprocessing
from pathlib import Path
import logging
import threading
import sys
import traceback
import queue

# Assuming the following imports are needed for the test setup
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def log_handler():
    # Create a temporary log file path
    temp_path = Path("test_logfile.log")
    handler = MultiprocessingFileHandler(temp_path, mode="w")
    yield handler
    # Clean up the log file after the test
    if temp_path.exists():
        temp_path.unlink()

def test_valid_case(log_handler):
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(log_handler)

    # Log a message from the main process
    logger.debug("Debug message from main process")

    # Create a separate process to log a message
    def log_from_process():
        logger = logging.getLogger("test_logger")
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug message from subprocess")

    p = multiprocessing.Process(target=log_from_process)
    p.start()
    p.join()

    # Check if the log file contains both messages
    with open(log_handler._path, 'r') as f:
        logs = f.readlines()
        assert len(logs) == 2, "Expected two log entries but got {}".format(len(logs))
        assert "Debug message from main process" in logs[0], "Main process log not found in the log file"
        assert "Debug message from subprocess" in logs[1], "Subprocess log not found in the log file"

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

log_handler = <MultiprocessingFileHandler (NOTSET)>

    def test_valid_case(log_handler):
        logger = logging.getLogger("test_logger")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(log_handler)
    
        # Log a message from the main process
        logger.debug("Debug message from main process")
    
        # Create a separate process to log a message
        def log_from_process():
            logger = logging.getLogger("test_logger")
            logger.setLevel(logging.DEBUG)
            logger.debug("Debug message from subprocess")
    
        p = multiprocessing.Process(target=log_from_process)
        p.start()
        p.join()
    
        # Check if the log file contains both messages
>       with open(log_handler._path, 'r') as f:
E       AttributeError: 'MultiprocessingFileHandler' object has no attribute '_path'

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_case.py:43: AttributeError
------------------------------ Captured log call -------------------------------
DEBUG    test_logger:test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_case.py:30 Debug message from main process
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.11s ===============================
"""