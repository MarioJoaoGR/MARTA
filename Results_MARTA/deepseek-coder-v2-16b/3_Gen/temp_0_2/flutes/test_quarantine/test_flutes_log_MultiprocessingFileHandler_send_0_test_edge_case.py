
import pytest
from flutes.log import MultiprocessingFileHandler
import multiprocessing
import logging
import threading

@pytest.fixture
def setup_logger():
    logger = logging.getLogger("test_logger")
    handler = MultiprocessingFileHandler('test_logfile.log')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return handler, logger

@pytest.mark.parametrize("message", ["Test message 1", "Another test message"])
def test_send_logs(setup_logger, message):
    handler, logger = setup_logger
    logger.info(message)
    
    # Check if the message is in the queue
    assert not handler.queue.empty()
    
    # Retrieve and check the log message from the queue
    logged_message = handler.queue.get_nowait()
    assert message in logged_message

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_edge_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_send_logs[Test message 1] ________________________

setup_logger = (<MultiprocessingFileHandler (NOTSET)>, <Logger test_logger (DEBUG)>)
message = 'Test message 1'

    @pytest.mark.parametrize("message", ["Test message 1", "Another test message"])
    def test_send_logs(setup_logger, message):
        handler, logger = setup_logger
        logger.info(message)
    
        # Check if the message is in the queue
>       assert not handler.queue.empty()
E       assert not True
E        +  where True = empty()
E        +    where empty = <multiprocessing.queues.Queue object at 0x7f588a21b510>.empty
E        +      where <multiprocessing.queues.Queue object at 0x7f588a21b510> = <MultiprocessingFileHandler (NOTSET)>.queue

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_edge_case.py:22: AssertionError
------------------------------ Captured log call -------------------------------
INFO     test_logger:test_flutes_log_MultiprocessingFileHandler_send_0_test_edge_case.py:19 Test message 1
_____________________ test_send_logs[Another test message] _____________________

setup_logger = (<MultiprocessingFileHandler (NOTSET)>, <Logger test_logger (DEBUG)>)
message = 'Another test message'

    @pytest.mark.parametrize("message", ["Test message 1", "Another test message"])
    def test_send_logs(setup_logger, message):
        handler, logger = setup_logger
        logger.info(message)
    
        # Check if the message is in the queue
>       assert not handler.queue.empty()
E       assert not True
E        +  where True = empty()
E        +    where empty = <multiprocessing.queues.Queue object at 0x7f588914edd0>.empty
E        +      where <multiprocessing.queues.Queue object at 0x7f588914edd0> = <MultiprocessingFileHandler (NOTSET)>.queue

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_edge_case.py:22: AssertionError
------------------------------ Captured log call -------------------------------
INFO     test_logger:test_flutes_log_MultiprocessingFileHandler_send_0_test_edge_case.py:19 Another test message
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_edge_case.py::test_send_logs[Test message 1]
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_edge_case.py::test_send_logs[Another test message]
============================== 2 failed in 0.10s ===============================
"""