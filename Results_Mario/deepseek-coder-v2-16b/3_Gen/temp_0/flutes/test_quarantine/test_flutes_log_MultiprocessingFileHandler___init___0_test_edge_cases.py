
import pytest
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler

def worker(queue):
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.QueueHandler(queue)
    logger.addHandler(handler)
    logger.debug("Test log message from worker")

@pytest.fixture
def setup_logger():
    log_path = Path("logs/app.log")
    queue = multiprocessing.Queue()
    handler = MultiprocessingFileHandler(log_path)
    yield handler, queue
    # Cleanup if necessary

def test_multiprocessing(setup_logger):
    handler, queue = setup_logger
    processes = [multiprocessing.Process(target=worker, args=(queue,)) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    # Read the log file and check if logs are present
    with open("logs/app.log", "r") as f:
        log_content = f.read()
        assert "Test log message from worker" in log_content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_edge_cases.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_multiprocessing ____________________

    @pytest.fixture
    def setup_logger():
        log_path = Path("logs/app.log")
        queue = multiprocessing.Queue()
>       handler = MultiprocessingFileHandler(log_path)

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_edge_cases.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/log.py:46: in __init__
    self._handler = logging.FileHandler(path, mode=mode)
/usr/local/lib/python3.11/logging/__init__.py:1181: in __init__
    StreamHandler.__init__(self, self._open())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'FileHandler' object has no attribute 'level'") raised in repr()] FileHandler object at 0x7f35166f5690>

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
ERROR flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_edge_cases.py::test_multiprocessing
=============================== 1 error in 0.10s ===============================

"""