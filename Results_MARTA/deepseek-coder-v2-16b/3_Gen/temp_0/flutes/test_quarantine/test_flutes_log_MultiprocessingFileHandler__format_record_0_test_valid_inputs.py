
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler

def worker(queue):
    logger = logging.getLogger("test_logger")
    handler = logging.handlers.QueueHandler(queue)
    logger.addHandler(handler)
    for i in range(5):
        logger.debug(f"Worker {i} is working!")

def test_valid_inputs():
    log_path = Path("logs/app.log")
    queue = multiprocessing.Queue()
    
    # Start the worker process
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    p.join()
    
    # Read the log file to check if messages were logged correctly
    with open(log_path, 'r') as f:
        logs = f.readlines()
    
    assert len(logs) == 5, "Expected 5 log messages but got different number"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        log_path = Path("logs/app.log")
        queue = multiprocessing.Queue()
    
        # Start the worker process
        p = multiprocessing.Process(target=worker, args=(queue,))
        p.start()
        p.join()
    
        # Read the log file to check if messages were logged correctly
        with open(log_path, 'r') as f:
            logs = f.readlines()
    
>       assert len(logs) == 5, "Expected 5 log messages but got different number"
E       AssertionError: Expected 5 log messages but got different number
E       assert 2339 == 5
E        +  where 2339 = len(['This is a test log message.\n', 'Worker 0 is working!\n', 'Worker 1 is working!\n', 'Worker 2 is working!\n', 'Worker 3 is working!\n', 'Worker 4 is working!\n', ...])

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0_test_valid_inputs.py:27: AssertionError
----------------------------- Captured stderr call -----------------------------
Process Process-1:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0_test_valid_inputs.py", line 9, in worker
    handler = logging.handlers.QueueHandler(queue)
              ^^^^^^^^^^^^^^^^
AttributeError: module 'logging' has no attribute 'handlers'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================

"""