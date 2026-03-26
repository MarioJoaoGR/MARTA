
import pytest
from flutes.log import MultiprocessingFileHandler
import logging
import multiprocessing
from pathlib import Path

def test_error_case():
    log_path = Path('test_logfile.log')
    handler = MultiprocessingFileHandler(log_path, mode='a')
    
    # Set up a logger with this handler
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    def worker_function():
        for i in range(5):
            logger.info("Log message number %s", i)
    
    # Create and start multiple processes
    processes = [multiprocessing.Process(target=worker_function) for _ in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    # Check the log file content
    with open(log_path, 'r') as f:
        logs = f.readlines()
    
    assert len(logs) == 15, "Expected 15 log messages but got {}".format(len(logs))
    
    for i in range(5):
        assert f"Log message number {i}" in logs[i*3], f"Log message number {i} not found in the log file."

    # Clean up the log file and logger
    log_path.unlink() if log_path.exists() else None

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        log_path = Path('test_logfile.log')
        handler = MultiprocessingFileHandler(log_path, mode='a')
    
        # Set up a logger with this handler
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
    
        def worker_function():
            for i in range(5):
                logger.info("Log message number %s", i)
    
        # Create and start multiple processes
        processes = [multiprocessing.Process(target=worker_function) for _ in range(3)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    
        # Check the log file content
        with open(log_path, 'r') as f:
            logs = f.readlines()
    
>       assert len(logs) == 15, "Expected 15 log messages but got {}".format(len(logs))
E       AssertionError: Expected 15 log messages but got 14
E       assert 14 == 15
E        +  where 14 = len(['Test message with placeholder value\n', 'Test message with placeholder value\n', 'Test message\n', 'Test log message\n', '2026-03-23 23:31:54,621 - INFO - This is a test log message\n', 'Test log message\n', ...])

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_error_case.py:32: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_error_case.py::test_error_case
============================== 1 failed in 0.14s ===============================
"""