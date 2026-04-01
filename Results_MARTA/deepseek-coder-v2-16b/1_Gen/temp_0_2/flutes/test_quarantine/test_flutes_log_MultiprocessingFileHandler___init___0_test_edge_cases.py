
import multiprocessing
import logging
from pathlib import Path
import threading
from flutes.log import MultiprocessingFileHandler

def test_multiprocessing_logging():
    # Create a logger instance
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create an in-memory queue to simulate the multiprocessing queue
    q = multiprocessing.Queue()
    
    # Create an instance of MultiprocessingFileHandler with a mock file path
    handler = MultiprocessingFileHandler('mock_logfile.log')
    handler.queue = q  # Assign the in-memory queue to the handler's queue attribute
    
    # Add the handler to the logger
    logger.addHandler(handler)
    
    # Start a new process to log a message from another process
    def target():
        logger.info('Test log message from subprocess')
    
    p = multiprocessing.Process(target=target)
    p.start()
    p.join()
    
    # Check if the message was logged correctly in the file
    with open('mock_logfile.log', 'r') as f:
        log_content = f.read()
        assert 'Test log message from subprocess' in log_content, "Log message not found in log file"

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_________________________ test_multiprocessing_logging _________________________

    def test_multiprocessing_logging():
        # Create a logger instance
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.DEBUG)
    
        # Create an in-memory queue to simulate the multiprocessing queue
        q = multiprocessing.Queue()
    
        # Create an instance of MultiprocessingFileHandler with a mock file path
        handler = MultiprocessingFileHandler('mock_logfile.log')
        handler.queue = q  # Assign the in-memory queue to the handler's queue attribute
    
        # Add the handler to the logger
        logger.addHandler(handler)
    
        # Start a new process to log a message from another process
        def target():
            logger.info('Test log message from subprocess')
    
        p = multiprocessing.Process(target=target)
        p.start()
        p.join()
    
        # Check if the message was logged correctly in the file
        with open('mock_logfile.log', 'r') as f:
            log_content = f.read()
>           assert 'Test log message from subprocess' in log_content, "Log message not found in log file"
E           AssertionError: Log message not found in log file
E           assert 'Test log message from subprocess' in ''

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_edge_cases.py:34: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_edge_cases.py::test_multiprocessing_logging
============================== 1 failed in 0.10s ===============================
"""