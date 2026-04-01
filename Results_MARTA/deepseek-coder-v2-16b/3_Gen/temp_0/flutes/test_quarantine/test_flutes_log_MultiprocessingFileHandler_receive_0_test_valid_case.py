
import pytest
import logging
from flutes.log import MultiprocessingFileHandler
import multiprocessing
import threading
import traceback
import sys
from unittest.mock import MagicMock

@pytest.fixture
def setup_logger():
    log_path = "test_logfile.log"
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    # Create a fake queue for the logger to use
    handler.queue = multiprocessing.Queue()
    
    return handler, logger

def test_valid_case(setup_logger):
    handler, logger = setup_logger
    
    # Create a fake record to be processed by the handler
    log_record = logging.LogRecord(
        name='test',
        level=logging.DEBUG,
        pathname='test',
        lineno=0,
        msg="Test message",
        args=(),
        exc_info=None
    )
    
    # Put the record into the queue to be processed by the handler thread
    logger.queue.put(log_record)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

setup_logger = (<MultiprocessingFileHandler (NOTSET)>, <Logger Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_case (DEBUG)>)

    def test_valid_case(setup_logger):
        handler, logger = setup_logger
    
        # Create a fake record to be processed by the handler
        log_record = logging.LogRecord(
            name='test',
            level=logging.DEBUG,
            pathname='test',
            lineno=0,
            msg="Test message",
            args=(),
            exc_info=None
        )
    
        # Put the record into the queue to be processed by the handler thread
>       logger.queue.put(log_record)
E       AttributeError: 'Logger' object has no attribute 'queue'

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_case.py:39: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.10s ===============================
"""