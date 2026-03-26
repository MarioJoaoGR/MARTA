
import pytest
from flutes.log import MultiprocessingFileHandler
import logging
import multiprocessing
import threading

@pytest.fixture(scope="module")
def setup_logger():
    # Create a logger instance with the custom handler
    logger = logging.getLogger(__name__)
    log_path = "test_logfile.log"
    handler = MultiprocessingFileHandler(log_path, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    yield logger  # provide the fixture value
    
    # Teardown: remove the handler to avoid memory leaks and other side effects
    for hdlr in logger.handlers[:]:
        logger.removeHandler(hdlr)

def test_valid_input(setup_logger):
    logger = setup_logger
    assert isinstance(logger, logging.Logger), "Logger instance is not correctly set up"
    
    # Example log message
    logger.info("This is a test log message")
    
    # Add assertions to check if the log file contains the expected log messages
    with open("test_logfile.log", "r") as f:
        logs = f.readlines()
        assert len(logs) > 0, "No logs were written"
        assert "This is a test log message" in logs[-1], "Log message not found or incorrect"

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

setup_logger = <Logger Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input (DEBUG)>

    def test_valid_input(setup_logger):
        logger = setup_logger
        assert isinstance(logger, logging.Logger), "Logger instance is not correctly set up"
    
        # Example log message
        logger.info("This is a test log message")
    
        # Add assertions to check if the log file contains the expected log messages
        with open("test_logfile.log", "r") as f:
            logs = f.readlines()
            assert len(logs) > 0, "No logs were written"
>           assert "This is a test log message" in logs[-1], "Log message not found or incorrect"
E           AssertionError: Log message not found or incorrect
E           assert 'This is a test log message' in 'Test log message\n'

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input.py:36: AssertionError
------------------------------ Captured log call -------------------------------
INFO     Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input:test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input.py:30 This is a test log message
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""