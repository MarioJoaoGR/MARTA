
import sys
import os
import pytest
from flutes.io import shut_up

@pytest.fixture(autouse=True)
def mock_stdout():
    # Mock sys.stdout to be a StringIO object during the test
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    yield
    sys.stdout.close()
    sys.stdout = original_stdout

def test_edge_case_none():
    with shut_up(stderr=False, stdout=False) as s:
        assert sys.stdout is None

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

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_edge_case_none.py FE  [100%]

==================================== ERRORS ====================================
___________________ ERROR at teardown of test_edge_case_none ___________________

self = <contextlib._GeneratorContextManager object at 0x7f2cc2d33d90>
typ = None, value = None, traceback = None

    def __exit__(self, typ, value, traceback):
        if typ is None:
            try:
>               next(self.gen)
E               ValueError: I/O operation on closed file.

/usr/local/lib/python3.11/contextlib.py:144: ValueError
=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with shut_up(stderr=False, stdout=False) as s:
>           assert sys.stdout is None
E           assert <_io.TextIOWrapper name="<_io.FileIO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'> is None
E            +  where <_io.TextIOWrapper name="<_io.FileIO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'> = sys.stdout

flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_edge_case_none.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_edge_case_none.py::test_edge_case_none
ERROR flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_edge_case_none.py::test_edge_case_none
========================== 1 failed, 1 error in 0.10s ==========================

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
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 685, in readouterr
    out = self.out.snap() if self.out else ""
          ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 570, in snap
    self.tmpfile.seek(0)
ValueError: I/O operation on closed file.
"""