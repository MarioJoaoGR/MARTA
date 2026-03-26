
import pytest
from flutes.log import MultiprocessingFileHandler
import logging
import multiprocessing as mp
import threading
from pathlib import Path

def test_invalid_inputs():
    with pytest.raises(FileNotFoundError):
        handler = MultiprocessingFileHandler('non_existent_path', 'r')

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(FileNotFoundError):
>           handler = MultiprocessingFileHandler('non_existent_path', 'r')

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/log.py:46: in __init__
    self._handler = logging.FileHandler(path, mode=mode)
/usr/local/lib/python3.11/logging/__init__.py:1181: in __init__
    StreamHandler.__init__(self, self._open())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'FileHandler' object has no attribute 'level'") raised in repr()] FileHandler object at 0x7f8c5ee51290>

    def _open(self):
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        open_func = self._builtin_open
>       return open_func(self.baseFilename, self.mode,
                         encoding=self.encoding, errors=self.errors)
E       IsADirectoryError: [Errno 21] Is a directory: '/projects/F202407648IACDCF2/mario/non_existent_path'

/usr/local/lib/python3.11/logging/__init__.py:1213: IsADirectoryError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.12s ===============================

Exception ignored in atexit callback: <function shutdown at 0x7f8c5fc4a840>
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 2186, in shutdown
    h.close()
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 92, in close
    self._handler.close()
    ^^^^^^^^^^^^^
AttributeError: 'MultiprocessingFileHandler' object has no attribute '_handler'
"""