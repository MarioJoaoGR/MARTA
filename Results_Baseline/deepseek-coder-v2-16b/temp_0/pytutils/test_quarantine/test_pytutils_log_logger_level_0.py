
import logging
import pytest
from pytutils.log import logger_level

# Create a logger instance
logger = logging.getLogger(__name__)

def test_logger_level_debug():
    """Test that debug messages are logged when the logger level is set to DEBUG."""
    log_handler = logging.StreamHandler()
    logger.addHandler(log_handler)
    
    with logger_level(logger, logging.DEBUG):
        logger.debug('This is a debug message.')  # This should be logged
        logger.info('This is an info message.')    # This should not be logged
    
    captured = log_handler.stream.getvalue().strip()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_log_logger_level_0.py F             [100%]

=================================== FAILURES ===================================
___________________________ test_logger_level_debug ____________________________

    def test_logger_level_debug():
        """Test that debug messages are logged when the logger level is set to DEBUG."""
        log_handler = logging.StreamHandler()
        logger.addHandler(log_handler)
    
        with logger_level(logger, logging.DEBUG):
            logger.debug('This is a debug message.')  # This should be logged
            logger.info('This is an info message.')    # This should not be logged
    
>       captured = log_handler.stream.getvalue().strip()
E       AttributeError: 'EncodedFile' object has no attribute 'getvalue'

pytutils/Test4DT_tests/test_pytutils_log_logger_level_0.py:18: AttributeError
----------------------------- Captured stderr call -----------------------------
This is a debug message.
This is an info message.
------------------------------ Captured log call -------------------------------
DEBUG    Test4DT_tests.test_pytutils_log_logger_level_0:test_pytutils_log_logger_level_0.py:15 This is a debug message.
INFO     Test4DT_tests.test_pytutils_log_logger_level_0:test_pytutils_log_logger_level_0.py:16 This is an info message.
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_logger_level_0.py::test_logger_level_debug
============================== 1 failed in 0.06s ===============================
"""