
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import multiprocessing as mp
import logging

# Assuming 'flutes.log' is the module where MultiprocessingFileHandler is defined
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def temp_log_file():
    # Create a temporary log file for testing
    return Path("test_logfile.log")

def test_edge_case_none(temp_log_file):
    with patch('flutes.log.mp.Queue', new=MagicMock()):
        handler = MultiprocessingFileHandler(temp_log_file)
        
        # Log a message to the queue
        log_message = "Test log message"
        handler.send(log_message)
        
        # Check if the message is in the queue
        assert handler.queue.get_nowait() == log_message

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

temp_log_file = PosixPath('test_logfile.log')

    def test_edge_case_none(temp_log_file):
        with patch('flutes.log.mp.Queue', new=MagicMock()):
            handler = MultiprocessingFileHandler(temp_log_file)
    
            # Log a message to the queue
            log_message = "Test log message"
            handler.send(log_message)
    
            # Check if the message is in the queue
>           assert handler.queue.get_nowait() == log_message
E           AssertionError: assert <MagicMock name='mock().get_nowait()' id='140390738825488'> == 'Test log message'
E            +  where <MagicMock name='mock().get_nowait()' id='140390738825488'> = <MagicMock name='mock().get_nowait' id='140390738886352'>()
E            +    where <MagicMock name='mock().get_nowait' id='140390738886352'> = <MagicMock name='mock()' id='140390739129168'>.get_nowait
E            +      where <MagicMock name='mock()' id='140390739129168'> = <MultiprocessingFileHandler (NOTSET)>.queue

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_1_test_edge_case_none.py:25: AssertionError
----------------------------- Captured stderr call -----------------------------
--- Logging error ---
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.21s ===============================

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
--- Logging error ---
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1113, in emit
    stream.write(msg + self.terminator)
TypeError: write() argument must be str, not MagicMock
Call stack:
  File "/usr/local/lib/python3.11/threading.py", line 1002, in _bootstrap
    self._bootstrap_inner()
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 61, in receive
    self._handler.emit(record)
Message: <MagicMock name='mock().get().msg' id='140390768875984'>
Arguments: <MagicMock name='mock().get().args' id='140390742133136'>
"""