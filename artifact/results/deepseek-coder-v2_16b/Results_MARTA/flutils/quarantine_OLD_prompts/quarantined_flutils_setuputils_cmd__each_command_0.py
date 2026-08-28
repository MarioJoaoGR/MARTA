
import pytest
from unittest.mock import patch, MagicMock
from flutils.setuputils.cmd import _each_command

def test_each_command_with_list():
    commands = ["ls -l", "cd /tmp"]
    result = list(_each_command(commands))
    assert result == [('/usr/bin/ls', '-l'), ('/bin/cd', '/tmp')]

def test_each_command_with_tuple():
    commands = ("ls -l", "cd /tmp")
    result = list(_each_command(commands))
    assert result == [('/usr/bin/ls', '-l'), ('/bin/cd', '/tmp')]

def test_each_command_with_empty_input():
    commands = []
    result = list(_each_command(commands))
    assert result == []

def test_each_command_with_whitespace():
    commands = [" python3 --version ", " echo Hello World "]
    result = list(_each_command(commands))
    assert result == [('/usr/bin/python3', '--version'), ('echo', 'Hello World')]

@patch('shlex.split')
def test_each_command_mocked_shlex_split(mock_shlex_split):
    mock_shlex_split.side_effect = [['/usr/bin/ls', '-l'], ['/bin/cd', '/tmp']]
    commands = ["ls -l", "cd /tmp"]
    result = list(_each_command(commands))
    assert result == [('/usr/bin/ls', '-l'), ('/bin/cd', '/tmp')]

@patch('flutils.setuputils.cmd._get_path')
def test_each_command_mocked_get_path(mock_get_path):
    mock_get_path.side_effect = ['/usr/bin/ls', '/bin/cd']
    commands = ["ls -l", "cd /tmp"]
    result = list(_each_command(commands))
    assert result == [('/usr/bin/ls', '-l'), ('/bin/cd', '/tmp')]

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