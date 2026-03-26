
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler

def test_valid_inputs():
    log_path = Path("test_logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    def worker(num):
        logger.debug(f"Worker {num} is working!")
    
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        log_path = Path("test_logs/app.log")
>       handler = MultiprocessingFileHandler(log_path)

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_valid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/log.py:46: in __init__
    self._handler = logging.FileHandler(path, mode=mode)
/usr/local/lib/python3.11/logging/__init__.py:1181: in __init__
    StreamHandler.__init__(self, self._open())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'FileHandler' object has no attribute 'level'") raised in repr()] FileHandler object at 0x7ffa0af37cd0>

    def _open(self):
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        open_func = self._builtin_open
>       return open_func(self.baseFilename, self.mode,
                         encoding=self.encoding, errors=self.errors)
E       FileNotFoundError: [Errno 2] No such file or directory: '/projects/F202407648IACDCF2/mario/test_logs/app.log'

/usr/local/lib/python3.11/logging/__init__.py:1213: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.14s ===============================

Exception ignored in atexit callback: <function shutdown at 0x7ffa0bfd2840>
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 2186, in shutdown
    h.close()
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 92, in close
    self._handler.close()
    ^^^^^^^^^^^^^
AttributeError: 'MultiprocessingFileHandler' object has no attribute '_handler'
"""