
import pytest
from unittest.mock import patch, MagicMock
import multiprocessing
import logging
from flutes.log import MultiprocessingFileHandler

@pytest.fixture
def setup_logger():
    logger = logging.getLogger(__name__)
    log_handler = MultiprocessingFileHandler('test_logfile.log')
    logger.addHandler(log_handler)
    return (logger, log_handler)

def test_valid_input(setup_logger):
    logger, log_handler = setup_logger

    # Mock the FileHandler to ensure it's not actually writing to a file
    with patch('logging.FileHandler') as mock_file_handler:
        mock_file_handler.return_value = MagicMock()

        logger.info("Test log message")

        # Check if the message was sent to the queue
        assert not log_handler.queue.empty(), "Log message should be in the queue"

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

setup_logger = (<Logger Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_send_0_test_valid_input (WARNING)>, <MultiprocessingFileHandler (NOTSET)>)

    def test_valid_input(setup_logger):
        logger, log_handler = setup_logger
    
        # Mock the FileHandler to ensure it's not actually writing to a file
        with patch('logging.FileHandler') as mock_file_handler:
            mock_file_handler.return_value = MagicMock()
    
            logger.info("Test log message")
    
            # Check if the message was sent to the queue
>           assert not log_handler.queue.empty(), "Log message should be in the queue"
E           AssertionError: Log message should be in the queue
E           assert not True
E            +  where True = empty()
E            +    where empty = <multiprocessing.queues.Queue object at 0x7fcd43758410>.empty
E            +      where <multiprocessing.queues.Queue object at 0x7fcd43758410> = <MultiprocessingFileHandler (NOTSET)>.queue

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_valid_input.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""