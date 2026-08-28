
import pytest
import os
import shutil
from flutils.setuputils.cmd import _get_path

def test_absolute_file_path():
    cmd = "/usr/bin/python3"
    path = _get_path(cmd)
    assert path == cmd

def test_command_name_in_path():
    cmd = "python3"
    with pytest.raises(FileNotFoundError, match=r'Unable to find the file path for the command: .*'):
        _get_path(cmd)

def test_non_existent_command():
    cmd = "nonexistentcommand"
    with pytest.raises(FileNotFoundError, match=r'Unable to find the file path for the command: .*'):
        _get_path(cmd)

def test_file_exists_but_no_execute_permissions():
    cmd = "/usr/bin/passwd"
    with pytest.raises(PermissionError, match=r'You do not have execute permission to run the file: .*'):
        _get_path(cmd)

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