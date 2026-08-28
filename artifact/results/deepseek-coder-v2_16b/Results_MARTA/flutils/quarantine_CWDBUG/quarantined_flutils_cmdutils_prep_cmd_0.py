
import pytest
from flutils.cmdutils import prep_cmd
from typing import Sequence, Tuple
from copy import copy
from shlex import split
from unittest.mock import patch

def test_prep_cmd_with_string():
    cmd = "ls -Flap"
    result = prep_cmd(cmd)
    assert isinstance(result, tuple), f"Expected a tuple but got {type(result)}"
    assert result == ('ls', '-Flap'), f"Expected ('ls', '-Flap') but got {result}"

def test_prep_cmd_with_bytes():
    cmd = b"echo Hello, World!"
    result = prep_cmd(cmd)
    assert isinstance(result, tuple), f"Expected a tuple but got {type(result)}"
    assert result == ('echo', 'Hello,', 'World!'), f"Expected ('echo', 'Hello,', 'World!') but got {result}"

def test_prep_cmd_with_list():
    cmd = ['ls', '-Flap']
    result = prep_cmd(cmd)
    assert isinstance(result, tuple), f"Expected a tuple but got {type(result)}"
    assert result == ('ls', '-Flap'), f"Expected ('ls', '-Flap') but got {result}"

def test_prep_cmd_with_tuple():
    cmd = ('ls', '-Flap')
    result = prep_cmd(cmd)
    assert isinstance(result, tuple), f"Expected a tuple but got {type(result)}"
    assert result == ('ls', '-Flap'), f"Expected ('ls', '-Flap') but got {result}"

def test_prep_cmd_raises_error_with_invalid_input():
    cmd = 12345  # Invalid input type
    with pytest.raises(TypeError):
        prep_cmd(cmd)

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