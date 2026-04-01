
import pytest
from flutes.log import MultiprocessingFileHandler

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test initializing with invalid mode type (number)
        handler = MultiprocessingFileHandler("logfile.log", 123)
    
    with pytest.raises(ValueError):
        # Test initializing with unsupported character in mode
        handler = MultiprocessingFileHandler("logfile.log", "x")

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            # Test initializing with invalid mode type (number)
            handler = MultiprocessingFileHandler("logfile.log", 123)
    
        with pytest.raises(ValueError):
            # Test initializing with unsupported character in mode
>           handler = MultiprocessingFileHandler("logfile.log", "x")

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/log.py:46: in __init__
    self._handler = logging.FileHandler(path, mode=mode)
/usr/local/lib/python3.11/logging/__init__.py:1181: in __init__
    StreamHandler.__init__(self, self._open())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'FileHandler' object has no attribute 'level'") raised in repr()] FileHandler object at 0x7f0e6f024110>

    def _open(self):
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        open_func = self._builtin_open
>       return open_func(self.baseFilename, self.mode,
                         encoding=self.encoding, errors=self.errors)
E       FileExistsError: [Errno 17] File exists: '/projects/F202407648IACDCF2/mario/logfile.log'

/usr/local/lib/python3.11/logging/__init__.py:1213: FileExistsError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================

Exception ignored in atexit callback: <function shutdown at 0x7f0e6fe0a700>
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 2186, in shutdown
    h.close()
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 92, in close
    self._handler.close()
    ^^^^^^^^^^^^^
AttributeError: 'MultiprocessingFileHandler' object has no attribute '_handler'
"""