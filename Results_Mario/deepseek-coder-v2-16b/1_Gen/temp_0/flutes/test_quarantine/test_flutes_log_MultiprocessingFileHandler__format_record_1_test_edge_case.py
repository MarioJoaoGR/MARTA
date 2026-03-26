
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler

def worker(logger):
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)

def test_edge_case():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    # Start the workers in separate processes
    processes = [multiprocessing.Process(target=worker, args=(logger,)) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    # Check if the log file contains expected messages
    with open("logs/app.log", "r") as f:
        logs = f.readlines()
    
    assert len(logs) == 5, f"Expected 5 log entries but got {len(logs)}"

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        log_path = Path("logs/app.log")
        handler = MultiprocessingFileHandler(log_path)
    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
    
        # Start the workers in separate processes
        processes = [multiprocessing.Process(target=worker, args=(logger,)) for _ in range(5)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    
        # Check if the log file contains expected messages
        with open("logs/app.log", "r") as f:
            logs = f.readlines()
    
>       assert len(logs) == 5, f"Expected 5 log entries but got {len(logs)}"
E       AssertionError: Expected 5 log entries but got 10
E       assert 10 == 5
E        +  where 10 = len(['Worker 0 is working!\n', 'Worker 1 is working!\n', 'Worker 2 is working!\n', 'Worker 3 is working!\n', 'Worker 4 is working!\n', 'Worker 1 is working!\n', ...])

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py:29: AssertionError
----------------------------- Captured stderr call -----------------------------
--- Logging error ---
--- Logging error ---
Traceback (most recent call last):
--- Logging error ---
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 84, in emit
    s = self._format_record(record)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 74, in _format_record
    record.msg = record.msg % record.args
                 ~~~~~~~~~~~^~~~~~~~~~~~~
Traceback (most recent call last):
TypeError: %d format: a real number is required, not str
Call stack:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 84, in emit
    s = self._format_record(record)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 74, in _format_record
    record.msg = record.msg % record.args
                 ~~~~~~~~~~~^~~~~~~~~~~~~
TypeError: %d format: a real number is required, not str
Call stack:
--- Logging error ---
Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 84, in emit
    s = self._format_record(record)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 74, in _format_record
    record.msg = record.msg % record.args
                 ~~~~~~~~~~~^~~~~~~~~~~~~
TypeError: %d format: a real number is required, not str
Call stack:
--- Logging error ---
Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 84, in emit
    s = self._format_record(record)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 74, in _format_record
    record.msg = record.msg % record.args
                 ~~~~~~~~~~~^~~~~~~~~~~~~
TypeError: %d format: a real number is required, not str
Call stack:
Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 84, in emit
    s = self._format_record(record)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 74, in _format_record
    record.msg = record.msg % record.args
                 ~~~~~~~~~~~^~~~~~~~~~~~~
TypeError: %d format: a real number is required, not str
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
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 21, in test_edge_case
    p.start()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 121, in start
    self._popen = self._Popen(self)
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 281, in _Popen
    return Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 19, in __init__
    self._launch(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 71, in _launch
    code = process_obj._bootstrap(parent_sentinel=child_r)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "<frozen runpy>", line 88, in _run_code
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 89, in emit
    self.handleError(record)
  File "/usr/local/lib/python3.11/site-packages/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 201, in console_main
    code = main()
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 175, in main
    ret: ExitCode | int = config.hook.pytest_cmdline_main(config=config)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
Message: 'Worker %d is working!'
Arguments: ('Process-1',)
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
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 21, in test_edge_case
    p.start()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 121, in start
    self._popen = self._Popen(self)
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 281, in _Popen
    return Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 19, in __init__
    self._launch(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 71, in _launch
    code = process_obj._bootstrap(parent_sentinel=child_r)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 89, in emit
    self.handleError(record)
Message: 'Worker %d is working!'
Arguments: ('Process-2',)
Process Process-1:
Process Process-2:
Traceback (most recent call last):
Traceback (most recent call last):
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 113, in pytest_runtest_protocol
    runtestprotocol(item, nextitem=nextitem)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 132, in runtestprotocol
    reports.append(call_and_report(item, "call", log))
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 241, in call_and_report
    call = CallInfo.from_call(
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 341, in from_call
    result: TResult | None = func()
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 242, in <lambda>
    lambda: runtest_hook(item=item, **kwds), when=when, reraise=reraise
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 386, in emit
    super().emit(record)
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1118, in emit
    self.handleError(record)
  File "/usr/local/lib/python3.11/site-packages/_pytest/runner.py", line 174, in pytest_runtest_call
    item.runtest()
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1110, in emit
    msg = self.format(record)
          ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/python.py", line 1627, in runtest
    self.ihook.pytest_pyfunc_call(pyfuncitem=self)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 953, in format
    return fmt.format(record)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 139, in format
    return super().format(record)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 687, in format
    record.message = record.getMessage()
                     ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 377, in getMessage
    msg = msg % self.args
          ~~~~^~~~~~~~~~~
  File "/usr/local/lib/python3.11/site-packages/_pytest/python.py", line 159, in pytest_pyfunc_call
    result = testfunction(**testargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 21, in test_edge_case
    p.start()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 121, in start
    self._popen = self._Popen(self)
TypeError: %d format: a real number is required, not str
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 281, in _Popen
    return Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 19, in __init__
    self._launch(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 71, in _launch
    code = process_obj._bootstrap(parent_sentinel=child_r)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 386, in emit
    super().emit(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1118, in emit
    self.handleError(record)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 89, in emit
    self.handleError(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1110, in emit
    msg = self.format(record)
          ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 953, in format
    return fmt.format(record)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 139, in format
    return super().format(record)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 687, in format
    record.message = record.getMessage()
                     ^^^^^^^^^^^^^^^^^^^
Message: 'Worker %d is working!'
Arguments: ('Process-3',)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 377, in getMessage
    msg = msg % self.args
          ~~~~^~~~~~~~~~~
TypeError: %d format: a real number is required, not str
Process Process-3:
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
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 21, in test_edge_case
    p.start()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 121, in start
    self._popen = self._Popen(self)
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 281, in _Popen
    return Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 19, in __init__
    self._launch(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 71, in _launch
    code = process_obj._bootstrap(parent_sentinel=child_r)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 89, in emit
    self.handleError(record)
Message: 'Worker %d is working!'
Arguments: ('Process-4',)
Traceback (most recent call last):
Process Process-4:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 386, in emit
    super().emit(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1118, in emit
    self.handleError(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1110, in emit
    msg = self.format(record)
          ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 953, in format
    return fmt.format(record)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 139, in format
    return super().format(record)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 687, in format
    record.message = record.getMessage()
                     ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 377, in getMessage
    msg = msg % self.args
          ~~~~^~~~~~~~~~~
TypeError: %d format: a real number is required, not str
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
Traceback (most recent call last):
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
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 21, in test_edge_case
    p.start()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 121, in start
    self._popen = self._Popen(self)
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/context.py", line 281, in _Popen
    return Popen(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 19, in __init__
    self._launch(process_obj)
  File "/usr/local/lib/python3.11/multiprocessing/popen_fork.py", line 71, in _launch
    code = process_obj._bootstrap(parent_sentinel=child_r)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/log.py", line 89, in emit
    self.handleError(record)
Message: 'Worker %d is working!'
Arguments: ('Process-5',)
Process Process-5:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 386, in emit
    super().emit(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1118, in emit
    self.handleError(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1110, in emit
    msg = self.format(record)
          ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 953, in format
    return fmt.format(record)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 139, in format
    return super().format(record)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 687, in format
    record.message = record.getMessage()
                     ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 377, in getMessage
    msg = msg % self.args
          ~~~~^~~~~~~~~~~
TypeError: %d format: a real number is required, not str
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py", line 8, in worker
    logger.debug("Worker %d is working!", multiprocessing.current_process().name)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1477, in debug
    self._log(DEBUG, msg, args, **kwargs)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1634, in _log
    self.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 978, in handle
    self.emit(record)
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 386, in emit
    super().emit(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1118, in emit
    self.handleError(record)
  File "/usr/local/lib/python3.11/logging/__init__.py", line 1110, in emit
    msg = self.format(record)
          ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 953, in format
    return fmt.format(record)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/logging.py", line 139, in format
    return super().format(record)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 687, in format
    record.message = record.getMessage()
                     ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/logging/__init__.py", line 377, in getMessage
    msg = msg % self.args
          ~~~~^~~~~~~~~~~
TypeError: %d format: a real number is required, not str
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.10s ===============================
"""