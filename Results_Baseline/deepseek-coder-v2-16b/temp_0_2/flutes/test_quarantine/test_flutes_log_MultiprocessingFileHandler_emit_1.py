
import pytest
import multiprocessing
import threading
import logging
from pathlib import Path
import queue as mp_queue
from flutes.log import MultiprocessingFileHandler

@pytest.fixture
def setup_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create an instance of the MultiprocessingFileHandler with default mode 'a'
    log_handler = MultiprocessingFileHandler(Path("logs/app.log"))
    
    # Add the handler to the logger
    logger.addHandler(log_handler)
    
    return logger, log_handler

def test_emit_with_valid_record(setup_logger):
    logger, log_handler = setup_logger
    record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
    # Mock the _format_record method to return a string
    log_handler._format_record = lambda r: "formatted_message"
    
    # Call emit with the record
    log_handler.emit(record)
    
    # Check that send was called with the formatted message
    assert log_handler.queue.put.called_once_with("formatted_message")

def test_emit_with_keyboard_interrupt(setup_logger):
    logger, log_handler = setup_logger
    record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
    # Mock the _format_record method to raise KeyboardInterrupt
    log_handler._format_record = lambda r: pytest.raises(KeyboardInterrupt)
    
    with pytest.raises(KeyboardInterrupt):
        log_handler.emit(record)

def test_emit_with_system_exit(setup_logger):
    logger, log_handler = setup_logger
    record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
    # Mock the _format_record method to raise SystemExit
    log_handler._format_record = lambda r: pytest.raises(SystemExit)
    
    with pytest.raises(SystemExit):
        log_handler.emit(record)

def test_emit_with_other_exception(setup_logger):
    logger, log_handler = setup_logger
    record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
    # Mock the _format_record method to raise a generic exception
    log_handler._format_record = lambda r: pytest.raises(Exception)
    
    with pytest.raises(Exception):
        log_handler.emit(record)

def test_emit_handles_error_correctly(setup_logger, caplog):  # Added caplog parameter
    logger, log_handler = setup_logger
    record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
    # Mock the _format_record method to raise an exception that is caught by handleError
    log_handler._format_record = lambda r: pytest.raises(Exception)
    log_handler.handleError = lambda e: print("handled error")  # Mock handleError
    
    log_handler.emit(record)
    
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py F [ 20%]
FFF.                                                                     [100%]

=================================== FAILURES ===================================
_________________________ test_emit_with_valid_record __________________________

setup_logger = (<Logger my_logger (DEBUG)>, <MultiprocessingFileHandler (NOTSET)>)

    def test_emit_with_valid_record(setup_logger):
        logger, log_handler = setup_logger
        record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
        # Mock the _format_record method to return a string
        log_handler._format_record = lambda r: "formatted_message"
    
        # Call emit with the record
        log_handler.emit(record)
    
        # Check that send was called with the formatted message
>       assert log_handler.queue.put.called_once_with("formatted_message")
E       AttributeError: 'function' object has no attribute 'called_once_with'

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py:34: AttributeError
______________________ test_emit_with_keyboard_interrupt _______________________

setup_logger = (<Logger my_logger (DEBUG)>, <MultiprocessingFileHandler (NOTSET)>)

    def test_emit_with_keyboard_interrupt(setup_logger):
        logger, log_handler = setup_logger
        record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
        # Mock the _format_record method to raise KeyboardInterrupt
        log_handler._format_record = lambda r: pytest.raises(KeyboardInterrupt)
    
>       with pytest.raises(KeyboardInterrupt):
E       Failed: DID NOT RAISE <class 'KeyboardInterrupt'>

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py:43: Failed
__________________________ test_emit_with_system_exit __________________________

setup_logger = (<Logger my_logger (DEBUG)>, <MultiprocessingFileHandler (NOTSET)>)

    def test_emit_with_system_exit(setup_logger):
        logger, log_handler = setup_logger
        record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
        # Mock the _format_record method to raise SystemExit
        log_handler._format_record = lambda r: pytest.raises(SystemExit)
    
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py:53: Failed
________________________ test_emit_with_other_exception ________________________

setup_logger = (<Logger my_logger (DEBUG)>, <MultiprocessingFileHandler (NOTSET)>)

    def test_emit_with_other_exception(setup_logger):
        logger, log_handler = setup_logger
        record = logging.LogRecord('name', logging.DEBUG, 'pathname', 10, 'message', (), None)
    
        # Mock the _format_record method to raise a generic exception
        log_handler._format_record = lambda r: pytest.raises(Exception)
    
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py:63: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py::test_emit_with_valid_record
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py::test_emit_with_keyboard_interrupt
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py::test_emit_with_system_exit
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_1.py::test_emit_with_other_exception
========================= 4 failed, 1 passed in 0.12s ==========================

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
AttributeError: 'str' object has no attribute 'getMessage'
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
AttributeError: 'RaisesContext' object has no attribute 'getMessage'
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
AttributeError: 'RaisesContext' object has no attribute 'getMessage'
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
AttributeError: 'RaisesContext' object has no attribute 'getMessage'
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
AttributeError: 'RaisesContext' object has no attribute 'getMessage'
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