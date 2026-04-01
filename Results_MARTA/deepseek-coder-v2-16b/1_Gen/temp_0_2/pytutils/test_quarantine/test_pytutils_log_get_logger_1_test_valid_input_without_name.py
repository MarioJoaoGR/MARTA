
import pytest
import logging
from pytutils.log import get_logger, _ensure_configured, _namespace_from_calling_context

@pytest.fixture(autouse=True)
def setup():
    # Mock the necessary functions to isolate the test
    def mock__ensure_configured():
        pass

    def mock__namespace_from_calling_context():
        return 'default_namespace'

    logging.getLogger = lambda name: f"MockedLogger_{name}"

    get_logger._ensure_configured = mock__ensure_configured
    get_logger._namespace_from_calling_context = mock__namespace_from_calling_context

def test_valid_input_without_name():
    log = get_logger()
    assert isinstance(log, logging.Logger)
    assert log.name == 'default_namespace'
    log.info('test')  # Ensure the logger can handle info messages without errors

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_log_get_logger_1_test_valid_input_without_name.py E
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 805, in pytest_runtestloop
INTERNALERROR>     return (yield)  # Run all the tests.
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/terminal.py", line 673, in pytest_runtestloop
INTERNALERROR>     result = yield
INTERNALERROR>              ^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 362, in pytest_runtestloop
INTERNALERROR>     item.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/warnings.py", line 112, in pytest_runtest_protocol
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/assertion/__init__.py", line 176, in pytest_runtest_protocol
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 53, in run_old_style_hookwrapper
INTERNALERROR>     return result.get_result()
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_result.py", line 103, in get_result
INTERNALERROR>     raise exc.with_traceback(tb)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 38, in run_old_style_hookwrapper
INTERNALERROR>     res = yield
INTERNALERROR>           ^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/unittest.py", line 429, in pytest_runtest_protocol
INTERNALERROR>     res = yield
INTERNALERROR>           ^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/faulthandler.py", line 87, in pytest_runtest_protocol
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 113, in pytest_runtest_protocol
INTERNALERROR>     runtestprotocol(item, nextitem=nextitem)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 137, in runtestprotocol
INTERNALERROR>     reports.append(call_and_report(item, "teardown", log, nextitem=nextitem))
INTERNALERROR>                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 244, in call_and_report
INTERNALERROR>     report: TestReport = ihook.pytest_runtest_makereport(item=item, call=call)
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/tmpdir.py", line 318, in pytest_runtest_makereport
INTERNALERROR>     rep = yield
INTERNALERROR>           ^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 152, in _multicall
INTERNALERROR>     teardown.send(result)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 43, in run_old_style_hookwrapper
INTERNALERROR>     teardown.send(result)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pytest_jsonreport/plugin.py", line 87, in pytest_runtest_makereport
INTERNALERROR>     item._json_report_extra[call.when].update(streams)
INTERNALERROR>     ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
INTERNALERROR> KeyError: 'teardown'
INTERNALERROR> 
INTERNALERROR> During handling of the above exception, another exception occurred:
INTERNALERROR> 
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 804, in pytest_runtestloop
INTERNALERROR>     with catching_logs(self.log_file_handler, level=self.log_file_level):
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 369, in __exit__
INTERNALERROR>     root_logger = logging.getLogger()
INTERNALERROR>                   ^^^^^^^^^^^^^^^^^^^
INTERNALERROR> TypeError: setup.<locals>.<lambda>() missing 1 required positional argument: 'name'
INTERNALERROR> 
INTERNALERROR> During handling of the above exception, another exception occurred:
INTERNALERROR> 
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 283, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 337, in _main
INTERNALERROR>     config.hook.pytest_runtestloop(session=session)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 803, in pytest_runtestloop
INTERNALERROR>     with catching_logs(self.log_cli_handler, level=self.log_cli_level):
INTERNALERROR>   File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 369, in __exit__
INTERNALERROR>     root_logger = logging.getLogger()
INTERNALERROR>                   ^^^^^^^^^^^^^^^^^^^
INTERNALERROR> TypeError: setup.<locals>.<lambda>() missing 1 required positional argument: 'name'

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.11/site-packages/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
                     ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 201, in console_main
    code = main()
           ^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 175, in main
    ret: ExitCode | int = config.hook.pytest_cmdline_main(config=config)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 330, in pytest_cmdline_main
    return wrap_session(config, _main)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 318, in wrap_session
    config.hook.pytest_sessionfinish(
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 116, in _multicall
    next(function_gen)  # first yield
    ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 868, in pytest_sessionfinish
    with catching_logs(self.log_cli_handler, level=self.log_cli_level):
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 354, in __enter__
    root_logger = logging.getLogger()
                  ^^^^^^^^^^^^^^^^^^^
TypeError: setup.<locals>.<lambda>() missing 1 required positional argument: 'name'
"""