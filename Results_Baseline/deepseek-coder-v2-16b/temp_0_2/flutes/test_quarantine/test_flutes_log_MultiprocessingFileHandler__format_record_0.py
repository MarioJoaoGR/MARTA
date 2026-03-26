
import pytest
import multiprocessing
import threading
import logging
from pathlib import Path
import os

# Import the function from the module
import flutes.log as mplh

@pytest.fixture(scope="module")
def logger():
    # Create a logger instance
    log = logging.getLogger('my_logger')
    log.setLevel(logging.DEBUG)
    return log

@pytest.fixture(scope="module")
def handler():
    # Create an instance of the MultiprocessingFileHandler
    path = Path("logs/app.log")
    hndlr = mplh.MultiprocessingFileHandler(path)
    yield hndlr
    # Clean up: remove the log file after tests are done
    if os.path.exists(path):
        os.remove(path)

def test_logger_adds_handler(logger, handler):
    logger.addHandler(handler)
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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0.py E [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_logger_adds_handler __________________

    @pytest.fixture(scope="module")
    def handler():
        # Create an instance of the MultiprocessingFileHandler
        path = Path("logs/app.log")
>       hndlr = mplh.MultiprocessingFileHandler(path)
E       AttributeError: 'function' object has no attribute 'MultiprocessingFileHandler'

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0.py:23: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0.py::test_logger_adds_handler
=============================== 1 error in 0.10s ===============================
"""