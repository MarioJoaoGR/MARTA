
import pytest
from httpie.internal.daemons import _spawn_posix
from unittest.mock import patch, MagicMock
import os
import sys
import platform
from contextlib import suppress

@pytest.mark.parametrize("args, process_context", [
    (['arg1', 'arg2'], {'VAR': 'value'}),
    ([], {}),
    (None, None)
])
def test_invalid_inputs(args, process_context):
    with patch('httpie.core.main', MagicMock()):
        if args is None or process_context is None:
            with pytest.raises(TypeError):
                _spawn_posix(args, process_context)
        else:
            # Mocking the fork and setsid functions to simulate the double-fork behavior
            def mock_fork():
                return 0 if os.fork() == 0 else 1

            with patch('os.fork', side_effect=mock_fork):
                with patch('os.setsid'):
                    _spawn_posix(args, process_context)

    # Ensure that the function handles invalid inputs correctly by raising a TypeError
    with pytest.raises(TypeError):
        _spawn_posix(None, None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py F [ 33%]
FF                                                                       [100%]FFE                                                                      [100%]E                                                                      [100%]

=================================== FAILURES ===================================
_________________ test_invalid_inputs[args0-process_context0] __________________

args = ['arg1', 'arg2'], process_context = {'VAR': 'value'}

    @pytest.mark.parametrize("args, process_context", [
        (['arg1', 'arg2'], {'VAR': 'value'}),
        ([], {}),
        (None, None)
    ])
    def test_invalid_inputs(args, process_context):
        with patch('httpie.core.main', MagicMock()):
            if args is None or process_context is None:
                with pytest.raises(TypeError):
                    _spawn_posix(args, process_context)
            else:
                # Mocking the fork and setsid functions to simulate the double-fork behavior
                def mock_fork():
                    return 0 if os.fork() == 0 else 1
    
                with patch('os.fork', side_effect=mock_fork):
                    with patch('os.setsid'):
>                       _spawn_posix(args, process_context)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/internal/daemons.py:67: in _spawn_posix
    pid = os.fork()
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1189: in _execute_mock_call
    result = effect(*args, **kwargs)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:23: in mock_fork
    return 0 if os.fork() == 0 else 1
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________ test_invalid_inputs[args1-process_context1] __________________

args = [], process_context = {}

    @pytest.mark.parametrize("args, process_context", [
        (['arg1', 'arg2'], {'VAR': 'value'}),
        ([], {}),
        (None, None)
    ])
    def test_invalid_inputs(args, process_context):
        with patch('httpie.core.main', MagicMock()):
            if args is None or process_context is None:
                with pytest.raises(TypeError):
                    _spawn_posix(args, process_context)
            else:
                # Mocking the fork and setsid functions to simulate the double-fork behavior
                def mock_fork():
                    return 0 if os.fork() == 0 else 1
    
                with patch('os.fork', side_effect=mock_fork):
                    with patch('os.setsid'):
>                       _spawn_posix(args, process_context)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/internal/daemons.py:67: in _spawn_posix
    pid = os.fork()
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1189: in _execute_mock_call
    result = effect(*args, **kwargs)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:23: in mock_fork
    return 0 if os.fork() == 0 else 1
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
________________________ test_invalid_inputs[None-None] ________________________

args = None, process_context = None

    @pytest.mark.parametrize("args, process_context", [
        (['arg1', 'arg2'], {'VAR': 'value'}),
        ([], {}),
        (None, None)
    ])
    def test_invalid_inputs(args, process_context):
        with patch('httpie.core.main', MagicMock()):
            if args is None or process_context is None:
>               with pytest.raises(TypeError):
E               Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[args0-process_context0]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[args1-process_context1]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[None-None]
============================== 3 failed in 0.44s ===============================


==================================== ERRORS ====================================
_____________ ERROR at teardown of test_invalid_inputs[None-None] ______________

self = <contextlib._GeneratorContextManager object at 0x7f3244416910>

    def __enter__(self):
        # do not keep args and kwds alive unnecessarily
        # they are only needed for recreation, which is not possible anymore
        del self.args, self.kwds, self.func
        try:
>           return next(self.gen)
E           ValueError: I/O operation on closed file

/usr/local/lib/python3.11/contextlib.py:137: ValueError
=================================== FAILURES ===================================
_________________ test_invalid_inputs[args0-process_context0] __________________

args = ['arg1', 'arg2'], process_context = {'VAR': 'value'}

    @pytest.mark.parametrize("args, process_context", [
        (['arg1', 'arg2'], {'VAR': 'value'}),
        ([], {}),
        (None, None)
    ])
    def test_invalid_inputs(args, process_context):
        with patch('httpie.core.main', MagicMock()):
            if args is None or process_context is None:
                with pytest.raises(TypeError):
                    _spawn_posix(args, process_context)
            else:
                # Mocking the fork and setsid functions to simulate the double-fork behavior
                def mock_fork():
                    return 0 if os.fork() == 0 else 1
    
                with patch('os.fork', side_effect=mock_fork):
                    with patch('os.setsid'):
>                       _spawn_posix(args, process_context)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/internal/daemons.py:67: in _spawn_posix
    pid = os.fork()
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1189: in _execute_mock_call
    result = effect(*args, **kwargs)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:23: in mock_fork
    return 0 if os.fork() == 0 else 1
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________ test_invalid_inputs[args1-process_context1] __________________

args = [], process_context = {}

    @pytest.mark.parametrize("args, process_context", [
        (['arg1', 'arg2'], {'VAR': 'value'}),
        ([], {}),
        (None, None)
    ])
    def test_invalid_inputs(args, process_context):
        with patch('httpie.core.main', MagicMock()):
            if args is None or process_context is None:
                with pytest.raises(TypeError):
                    _spawn_posix(args, process_context)
            else:
                # Mocking the fork and setsid functions to simulate the double-fork behavior
                def mock_fork():
                    return 0 if os.fork() == 0 else 1
    
                with patch('os.fork', side_effect=mock_fork):
                    with patch('os.setsid'):
>                       _spawn_posix(args, process_context)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/internal/daemons.py:67: in _spawn_posix
    pid = os.fork()
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1189: in _execute_mock_call
    result = effect(*args, **kwargs)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:23: in mock_fork
    return 0 if os.fork() == 0 else 1
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
________________________ test_invalid_inputs[None-None] ________________________

args = None, process_context = None

    @pytest.mark.parametrize("args, process_context", [
        (['arg1', 'arg2'], {'VAR': 'value'}),
        ([], {}),
        (None, None)
    ])
    def test_invalid_inputs(args, process_context):
        with patch('httpie.core.main', MagicMock()):
            if args is None or process_context is None:
                with pytest.raises(TypeError):
                    _spawn_posix(args, process_context)
            else:
                # Mocking the fork and setsid functions to simulate the double-fork behavior
                def mock_fork():
                    return 0 if os.fork() == 0 else 1
    
                with patch('os.fork', side_effect=mock_fork):
                    with patch('os.setsid'):
                        _spawn_posix(args, process_context)
    
        # Ensure that the function handles invalid inputs correctly by raising a TypeError
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:30: Failed

During handling of the above exception, another exception occurred:

self = <contextlib._GeneratorContextManager object at 0x7f3244500910>
typ = <class 'Failed'>, value = DID NOT RAISE <class 'TypeError'>
traceback = <traceback object at 0x7f3244502a00>

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
E               ValueError: I/O operation on closed file.

/usr/local/lib/python3.11/contextlib.py:158: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[args0-process_context0]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[args1-process_context1]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[None-None]
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[None-None]
========================== 3 failed, 1 error in 0.46s ==========================


==================================== ERRORS ====================================
_____________ ERROR at teardown of test_invalid_inputs[None-None] ______________

self = <contextlib._GeneratorContextManager object at 0x7f3245583310>

    def __enter__(self):
        # do not keep args and kwds alive unnecessarily
        # they are only needed for recreation, which is not possible anymore
        del self.args, self.kwds, self.func
        try:
>           return next(self.gen)
E           ValueError: I/O operation on closed file

/usr/local/lib/python3.11/contextlib.py:137: ValueError
=================================== FAILURES ===================================
_________________ test_invalid_inputs[args0-process_context0] __________________

args = ['arg1', 'arg2'], process_context = {'VAR': 'value'}

    @pytest.mark.parametrize("args, process_context", [
        (['arg1', 'arg2'], {'VAR': 'value'}),
        ([], {}),
        (None, None)
    ])
    def test_invalid_inputs(args, process_context):
        with patch('httpie.core.main', MagicMock()):
            if args is None or process_context is None:
                with pytest.raises(TypeError):
                    _spawn_posix(args, process_context)
            else:
                # Mocking the fork and setsid functions to simulate the double-fork behavior
                def mock_fork():
                    return 0 if os.fork() == 0 else 1
    
                with patch('os.fork', side_effect=mock_fork):
                    with patch('os.setsid'):
>                       _spawn_posix(args, process_context)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/internal/daemons.py:67: in _spawn_posix
    pid = os.fork()
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1189: in _execute_mock_call
    result = effect(*args, **kwargs)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:23: in mock_fork
    return 0 if os.fork() == 0 else 1
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________ test_invalid_inputs[args1-process_context1] __________________

args = [], process_context = {}

    @pytest.mark.parametrize("args, process_context", [
        (['arg1', 'arg2'], {'VAR': 'value'}),
        ([], {}),
        (None, None)
    ])
    def test_invalid_inputs(args, process_context):
        with patch('httpie.core.main', MagicMock()):
            if args is None or process_context is None:
                with pytest.raises(TypeError):
                    _spawn_posix(args, process_context)
            else:
                # Mocking the fork and setsid functions to simulate the double-fork behavior
                def mock_fork():
                    return 0 if os.fork() == 0 else 1
    
                with patch('os.fork', side_effect=mock_fork):
                    with patch('os.setsid'):
>                       _spawn_posix(args, process_context)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/internal/daemons.py:67: in _spawn_posix
    pid = os.fork()
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1189: in _execute_mock_call
    result = effect(*args, **kwargs)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py:23: in mock_fork
    return 0 if os.fork() == 0 else 1
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
________________________ test_invalid_inputs[None-None] ________________________

self = <contextlib._GeneratorContextManager object at 0x7f3244500910>
typ = None, value = None, traceback = None

    def __exit__(self, typ, value, traceback):
        if typ is None:
            try:
>               next(self.gen)
E               ValueError: I/O operation on closed file.

/usr/local/lib/python3.11/contextlib.py:144: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[args0-process_context0]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[args1-process_context1]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[None-None]
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemons__spawn_posix_3_test_invalid_inputs.py::test_invalid_inputs[None-None]
========================== 3 failed, 1 error in 0.46s ==========================

Traceback (most recent call last):
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.11/site-packages/pytest/__main__.py", line 9, in <module>
  File "/usr/local/lib/python3.11/site-packages/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
    raise SystemExit(pytest.console_main())
                     ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 201, in console_main
                     ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 201, in console_main
    code = main()
    code = main()
           ^^^^^^
           ^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 175, in main
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 175, in main
    ret: ExitCode | int = config.hook.pytest_cmdline_main(config=config)
    ret: ExitCode | int = config.hook.pytest_cmdline_main(config=config)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
  File "/usr/local/lib/python3.11/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 167, in _multicall
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 167, in _multicall
    raise exception
    raise exception
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
  File "/usr/local/lib/python3.11/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
    res = hook_impl.function(*args)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 330, in pytest_cmdline_main
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 330, in pytest_cmdline_main
    return wrap_session(config, _main)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    return wrap_session(config, _main)
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 325, in wrap_session
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/main.py", line 325, in wrap_session
    config._ensure_unconfigure()
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 1127, in _ensure_unconfigure
    config._ensure_unconfigure()
  File "/usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py", line 1127, in _ensure_unconfigure
    fin()
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 757, in stop_global_capturing
    fin()
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 757, in stop_global_capturing
    self._global_capturing.pop_outerr_to_orig()
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 638, in pop_outerr_to_orig
    self._global_capturing.pop_outerr_to_orig()
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 638, in pop_outerr_to_orig
    out, err = self.readouterr()
               ^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 685, in readouterr
    out, err = self.readouterr()
               ^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 685, in readouterr
    out = self.out.snap() if self.out else ""
          ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 570, in snap
    out = self.out.snap() if self.out else ""
          ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/_pytest/capture.py", line 570, in snap
    self.tmpfile.seek(0)
ValueError: I/O operation on closed file.
    self.tmpfile.seek(0)
ValueError: I/O operation on closed file.
"""