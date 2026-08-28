
import pytest
from flutils.cmdutils import RunCmd, CompletedProcess
from subprocess import run, PIPE, ChildProcessError
from unittest.mock import patch
import shlex
import os

# Test 1: Default Settings
def test_default_settings():
    with patch('flutils.cmdutils.subprocess') as mock_subprocess:
        mock_subprocess.run.return_value = CompletedProcess(0, '', '', '')
        cmd = RunCmd()
        result = cmd("ls -l")
        assert isinstance(result, CompletedProcess)
        mock_subprocess.run.assert_called_once_with("ls -l", **cmd.default_kwargs._asdict())

# Test 2: Custom Settings with raise_error=False and custom output encoding
def test_custom_settings():
    with patch('flutils.cmdutils.subprocess') as mock_subprocess:
        mock_subprocess.run.return_value = CompletedProcess(0, '', '', '')
        cmd_no_error = RunCmd(raise_error=False, output_encoding="utf-8")
        result_custom = cmd_no_error("ls -l", capture_output=True)
        assert isinstance(result_custom, CompletedProcess)
        mock_subprocess.run.assert_called_once_with("ls -l", **cmd_no_error.default_kwargs._asdict())

# Test 3: Using Default Keyword Arguments with custom command
def test_using_default_keyword_arguments():
    with patch('flutils.cmdutils.subprocess') as mock_subprocess:
        mock_subprocess.run.return_value = CompletedProcess(0, '', '', '')
        run_command = RunCmd(stdout=PIPE, stderr=PIPE)
        result = run_command('ls -flap %s' % os.getcwd())
        assert isinstance(result, CompletedProcess)
        mock_subprocess.run.assert_called_once_with('ls -flap %s' % os.getcwd(), **run_command.default_kwargs._asdict())

# Test 4: Specifying Additional Keyword Arguments with custom command and cwd
def test_specifying_additional_keyword_arguments():
    with patch('flutils.cmdutils.subprocess') as mock_subprocess:
        mock_subprocess.run.return_value = CompletedProcess(0, '', '', '')
        run_command = RunCmd(stdout=PIPE, stderr=PIPE, cwd=os.getcwd())
        result = run_command('ls -flap %s' % os.getcwd())
        assert isinstance(result, CompletedProcess)
        mock_subprocess.run.assert_called_once_with('ls -flap %s' % os.getcwd(), **run_command.default_kwargs._asdict())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
Traceback (most recent call last):
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/data/pydeps/marta/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 201, in console_main
    code = main()
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 156, in main
    config = _prepareconfig(args, plugins)
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 332, in _prepareconfig
    config = get_config(args, plugins)
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 293, in get_config
    dir=pathlib.Path.cwd(),
  File "/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py", line 993, in cwd
    return cls(cls._accessor.getcwd())
FileNotFoundError: [Errno 2] No such file or directory
"""