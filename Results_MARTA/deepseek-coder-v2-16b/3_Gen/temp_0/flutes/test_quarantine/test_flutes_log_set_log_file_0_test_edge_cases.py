
import logging
from pathlib import Path
from flutes.log import set_log_file, LOGGER  # Assuming the function and logger are defined in this module

def test_set_log_file():
    log_path = Path("test_logs/application.log")
    fmt = "%(asctime)s - %(levelname)s - %(message)s"
    
    # Call the function to set the log file
    set_log_file(log_path, fmt=fmt)
    
    # Check if the logger has a handler
    assert len(LOGGER.handlers) == 1
    
    # Check if the handler is of the correct type
    handler = LOGGER.handlers[0]
    assert isinstance(handler, logging.FileHandler), "Handler should be a FileHandler"
    
    # Check if the formatter is correctly set
    assert isinstance(handler.formatter, logging.Formatter)
    assert handler.formatter._fmt == fmt

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________________ test_set_log_file _______________________________

    def test_set_log_file():
        log_path = Path("test_logs/application.log")
        fmt = "%(asctime)s - %(levelname)s - %(message)s"
    
        # Call the function to set the log file
>       set_log_file(log_path, fmt=fmt)

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_edge_cases.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/log.py:146: in set_log_file
    handler = MultiprocessingFileHandler(path, mode="a")
flutes/flutes/log.py:46: in __init__
    self._handler = logging.FileHandler(path, mode=mode)
/usr/local/lib/python3.11/logging/__init__.py:1181: in __init__
    StreamHandler.__init__(self, self._open())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'FileHandler' object has no attribute 'level'") raised in repr()] FileHandler object at 0x7f6b0d28c590>

    def _open(self):
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        open_func = self._builtin_open
>       return open_func(self.baseFilename, self.mode,
                         encoding=self.encoding, errors=self.errors)
E       FileNotFoundError: [Errno 2] No such file or directory: '/projects/F202407648IACDCF2/mario/test_logs/application.log'

/usr/local/lib/python3.11/logging/__init__.py:1213: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_edge_cases.py::test_set_log_file
============================== 1 failed in 0.12s ===============================

"""