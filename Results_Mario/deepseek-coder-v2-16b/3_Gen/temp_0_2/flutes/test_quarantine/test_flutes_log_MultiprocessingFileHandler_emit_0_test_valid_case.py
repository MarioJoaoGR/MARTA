
import logging
from unittest.mock import MagicMock
import pytest
import multiprocessing as mp
import threading
from pathlib import Path

# Assuming the MultiprocessingFileHandler class is defined in flutes/log.py
from flutes.log import MultiprocessingFileHandler

@pytest.fixture
def log_handler():
    return MultiprocessingFileHandler('test_logfile.log')

def test_emit_valid_record(log_handler):
    # Mock the logging record
    record = logging.LogRecord(
        name='test',
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Test message",
        args=(),
        exc_info=None
    )
    
    # Mock the _format_record method to return a string
    log_handler._format_record = MagicMock(return_value="formatted_string")
    
    # Call emit with the mocked record
    log_handler.emit(record)
    
    # Assert that send was called once with the formatted string
    assert log_handler.send.call_count == 1
    log_handler.send.assert_called_once_with("formatted_string")

def test_emit_exception(log_handler):
    # Mock the logging record
    record = logging.LogRecord(
        name='test',
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Test message",
        args=(),
        exc_info=None
    )
    
    # Mock the _format_record method to raise an exception
    log_handler._format_record = MagicMock(side_effect=Exception("Format error"))
    
    # Call emit with the mocked record
    log_handler.emit(record)
    
    # Assert that handleError was called once with the record
    assert log_handler.handleError.call_count == 1
    log_handler.handleError.assert_called_once_with(record)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_emit_valid_record ____________________________

log_handler = <MultiprocessingFileHandler (NOTSET)>

    def test_emit_valid_record(log_handler):
        # Mock the logging record
        record = logging.LogRecord(
            name='test',
            level=logging.INFO,
            pathname=__file__,
            lineno=1,
            msg="Test message",
            args=(),
            exc_info=None
        )
    
        # Mock the _format_record method to return a string
        log_handler._format_record = MagicMock(return_value="formatted_string")
    
        # Call emit with the mocked record
        log_handler.emit(record)
    
        # Assert that send was called once with the formatted string
>       assert log_handler.send.call_count == 1
E       AttributeError: 'function' object has no attribute 'call_count'

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py:35: AttributeError
_____________________________ test_emit_exception ______________________________

log_handler = <MultiprocessingFileHandler (NOTSET)>

    def test_emit_exception(log_handler):
        # Mock the logging record
        record = logging.LogRecord(
            name='test',
            level=logging.INFO,
            pathname=__file__,
            lineno=1,
            msg="Test message",
            args=(),
            exc_info=None
        )
    
        # Mock the _format_record method to raise an exception
        log_handler._format_record = MagicMock(side_effect=Exception("Format error"))
    
        # Call emit with the mocked record
        log_handler.emit(record)
    
        # Assert that handleError was called once with the record
>       assert log_handler.handleError.call_count == 1
E       AttributeError: 'function' object has no attribute 'call_count'

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py:57: AttributeError
----------------------------- Captured stderr call -----------------------------
--- Logging error ---
Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 84, in emit
    s = self._format_record(record)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/unittest/mock.py", line 1124, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/unittest/mock.py", line 1128, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/unittest/mock.py", line 1183, in _execute_mock_call
    raise effect
Exception: Format error
Call stack:
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.11/site-packages/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 201, in console_main
    code = main()
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 175, in main
    ret: ExitCode | int = config.hook.pytest_cmdline_main(config=config)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 330, in pytest_cmdline_main
    return wrap_session(config, _main)
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 283, in wrap_session
    session.exitstatus = doit(config, session) or 0
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 337, in _main
    config.hook.pytest_runtestloop(session=session)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 362, in pytest_runtestloop
    item.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 113, in pytest_runtest_protocol
    runtestprotocol(item, nextitem=nextitem)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 132, in runtestprotocol
    reports.append(call_and_report(item, "call", log))
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 241, in call_and_report
    call = CallInfo.from_call(
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 341, in from_call
    result: TResult | None = func()
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 242, in <lambda>
    lambda: runtest_hook(item=item, **kwds), when=when, reraise=reraise
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 174, in pytest_runtest_call
    item.runtest()
  File "/usr/local/lib/python3.11/site-packages/_pytest/python.py", line 1627, in runtest
    self.ihook.pytest_pyfunc_call(pyfuncitem=self)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.11/site-packages/_pytest/python.py", line 159, in pytest_pyfunc_call
    result = testfunction(**testargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py", line 54, in test_emit_exception
    log_handler.emit(record)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 89, in emit
    self.handleError(record)
Message: 'Test message'
Arguments: ()
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py::test_emit_valid_record
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py::test_emit_exception
============================== 2 failed in 0.11s ===============================

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
"""