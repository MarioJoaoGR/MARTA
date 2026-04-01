
import pytest
import logging
from flutes.log import MultiprocessingFileHandler

def test_invalid_input():
    # Create an instance of MultiprocessingFileHandler with a valid log file path and mode
    handler = MultiprocessingFileHandler("logs/app.log", "a")
    
    # Send an invalid log message (non-string)
    with pytest.raises(TypeError):
        handler.send(12345)  # Sending an integer, which should raise a TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_4_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Create an instance of MultiprocessingFileHandler with a valid log file path and mode
        handler = MultiprocessingFileHandler("logs/app.log", "a")
    
        # Send an invalid log message (non-string)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_4_test_invalid_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_4_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================

--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1110, in emit
    msg = self.format(record)
          ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 953, in format
    return fmt.format(record)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 687, in format
    record.message = record.getMessage()
                     ^^^^^^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'getMessage'
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Unable to print the message and arguments - possible formatting error.
Use the traceback above to help find the error.
"""