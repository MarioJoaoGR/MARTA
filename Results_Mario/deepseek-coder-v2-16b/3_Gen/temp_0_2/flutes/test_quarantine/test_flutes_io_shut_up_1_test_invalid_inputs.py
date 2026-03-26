
import sys
import os
import pytest
from flutes.io import shut_up

def test_shut_up_invalid_inputs():
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    with pytest.raises(ValueError):
        with shut_up(stderr=True, stdout=False) as s:
            print("This should not be printed")  # This line should not be executed
            assert False, "Expected a ValueError"

    # Restore original stdout and stderr
    sys.stdout = original_stdout
    sys.stderr = original_stderr

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

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_inputs.py FE  [100%]

==================================== ERRORS ====================================
_______________ ERROR at teardown of test_shut_up_invalid_inputs _______________

self = <contextlib._GeneratorContextManager object at 0x7fe7e3b11ed0>
typ = None, value = None, traceback = None

    def __exit__(self, typ, value, traceback):
        if typ is None:
            try:
>               next(self.gen)
E               OSError: [Errno 22] Invalid argument

/usr/local/lib/python3.11/contextlib.py:144: OSError
=================================== FAILURES ===================================
_________________________ test_shut_up_invalid_inputs __________________________

    def test_shut_up_invalid_inputs():
        original_stdout = sys.stdout
        original_stderr = sys.stderr
    
        with pytest.raises(ValueError):
            with shut_up(stderr=True, stdout=False) as s:
                print("This should not be printed")  # This line should not be executed
>               assert False, "Expected a ValueError"
E               AssertionError: Expected a ValueError
E               assert False

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_inputs.py:14: AssertionError

During handling of the above exception, another exception occurred:

self = <contextlib._GeneratorContextManager object at 0x7fe7e3b13dd0>
typ = <class 'AssertionError'>
value = AssertionError('Expected a ValueError\nassert False')
traceback = <traceback object at 0x7fe7e3cef500>

    def __exit__(self, typ, value, traceback):
        if typ is None:
            try:
                next(self.gen)
            except StopIteration:
                return False
            else:
                try:
                    raise RuntimeError("generator didn't stop")
                finally:
                    self.gen.close()
        else:
            if value is None:
                # Need to force instantiation so we can reliably
                # tell if we get the same exception back
                value = typ()
            try:
>               self.gen.throw(typ, value, traceback)
E               OSError: [Errno 22] Invalid argument

/usr/local/lib/python3.11/contextlib.py:158: OSError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_inputs.py::test_shut_up_invalid_inputs
ERROR flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_inputs.py::test_shut_up_invalid_inputs
========================== 1 failed, 1 error in 0.12s ==========================

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
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 325, in wrap_session
    config._ensure_unconfigure()
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 1127, in _ensure_unconfigure
    fin()
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 757, in stop_global_capturing
    self._global_capturing.pop_outerr_to_orig()
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 638, in pop_outerr_to_orig
    out, err = self.readouterr()
               ^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 686, in readouterr
    err = self.err.snap() if self.err else ""
          ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 573, in snap
    self.tmpfile.truncate()
OSError: [Errno 22] Invalid argument
"""