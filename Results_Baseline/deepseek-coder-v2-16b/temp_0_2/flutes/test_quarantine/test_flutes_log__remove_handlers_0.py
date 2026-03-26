
import logging
import pytest
from flutes.log import _remove_handlers

def test_remove_handlers():
    # Create a logger instance
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    # Add some handlers (for example purposes only)
    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler('/path/to/logfile.log')
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    
    # Call the function to remove all handlers
    _remove_handlers(logger)
    
    # Assert that there are no more handlers in the logger
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

flutes/Test4DT_tests/test_flutes_log__remove_handlers_0.py F             [100%]

=================================== FAILURES ===================================
_____________________________ test_remove_handlers _____________________________

    def test_remove_handlers():
        # Create a logger instance
        logger = logging.getLogger('my_logger')
        logger.setLevel(logging.DEBUG)
    
        # Add some handlers (for example purposes only)
        handler1 = logging.StreamHandler()
>       handler2 = logging.FileHandler('/path/to/logfile.log')

flutes/Test4DT_tests/test_flutes_log__remove_handlers_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/logging/__init__.py:1181: in __init__
    StreamHandler.__init__(self, self._open())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'FileHandler' object has no attribute 'level'") raised in repr()] FileHandler object at 0x7f7e4a86cc90>

    def _open(self):
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        open_func = self._builtin_open
>       return open_func(self.baseFilename, self.mode,
                         encoding=self.encoding, errors=self.errors)
E       FileNotFoundError: [Errno 2] No such file or directory: '/path/to/logfile.log'

/usr/local/lib/python3.11/logging/__init__.py:1213: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log__remove_handlers_0.py::test_remove_handlers
============================== 1 failed in 0.12s ===============================
"""