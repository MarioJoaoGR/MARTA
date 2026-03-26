
import multiprocessing
import logging
from pathlib import Path
from unittest.mock import patch
import pytest
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield logger
    # Clean up the logger after the test
    for h in logger.handlers:
        logger.removeHandler(h)

def worker(logger):
    while True:
        logger.debug("Debug message from process")

@patch('multiprocessing.Process', autospec=True)
def test_valid_input(mock_process, logger):
    processes = [multiprocessing.Process(target=worker, args=(logger,)) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________

    @pytest.fixture(scope="module")
    def logger():
        log_path = Path("logs/app.log")
>       handler = MultiprocessingFileHandler(log_path)

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/log.py:46: in __init__
    self._handler = logging.FileHandler(path, mode=mode)
/usr/local/lib/python3.11/logging/__init__.py:1181: in __init__
    StreamHandler.__init__(self, self._open())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'FileHandler' object has no attribute 'level'") raised in repr()] FileHandler object at 0x7f5035686690>

    def _open(self):
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        open_func = self._builtin_open
>       return open_func(self.baseFilename, self.mode,
                         encoding=self.encoding, errors=self.errors)
E       FileNotFoundError: [Errno 2] No such file or directory: '/projects/F202407648IACDCF2/mario/logs/app.log'

/usr/local/lib/python3.11/logging/__init__.py:1213: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_input.py::test_valid_input
=============================== 1 error in 0.10s ===============================

"""