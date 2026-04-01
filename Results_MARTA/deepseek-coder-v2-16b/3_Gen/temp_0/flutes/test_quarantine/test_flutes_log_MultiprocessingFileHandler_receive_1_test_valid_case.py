
import multiprocessing
import logging
from pathlib import Path
from flutes.log import MultiprocessingFileHandler
from unittest.mock import patch, MagicMock
import pytest

@pytest.fixture(scope="module")
def setup_logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield (handler, logger)
    # Clean up resources if necessary

def test_valid_case(setup_logger):
    handler, logger = setup_logger

    # Mock a log record
    with patch('flutes.log.logging.LogRecord', autospec=True) as mock_record:
        mock_record.name = __name__
        mock_record.levelno = logging.DEBUG
        mock_record.msg = "Worker 1 is working!"

        # Put the record into the queue
        handler.queue.put(mock_record)

        # Check if the record was processed by the handler
        assert len(handler.queue) == 0, "Queue should be empty after processing"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_1_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

setup_logger = (<MultiprocessingFileHandler (NOTSET)>, <Logger Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_receive_1_test_valid_case (DEBUG)>)

    def test_valid_case(setup_logger):
        handler, logger = setup_logger
    
        # Mock a log record
        with patch('flutes.log.logging.LogRecord', autospec=True) as mock_record:
            mock_record.name = __name__
            mock_record.levelno = logging.DEBUG
            mock_record.msg = "Worker 1 is working!"
    
            # Put the record into the queue
            handler.queue.put(mock_record)
    
            # Check if the record was processed by the handler
>           assert len(handler.queue) == 0, "Queue should be empty after processing"
E           TypeError: object of type 'Queue' has no len()

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_1_test_valid_case.py:32: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_1_test_valid_case.py::test_valid_case
============================== 1 failed in 0.10s ===============================

"""