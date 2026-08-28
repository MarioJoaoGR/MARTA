
import pytest
from pathlib import Path
from flutils.pathutils import _normalize_path_pathlib
from unittest.mock import patch, MagicMock

def test_normalize_relative_path():
    with patch('flutils.pathutils._normalize_path', return_value=Path('/home/test_user/tmp/bar')):
        relative_path = Path('~/tmp/foo/../bar')
        normalized_relative_path = _normalize_path_pathlib(relative_path)
        assert str(normalized_relative_path) == '/home/test_user/tmp/bar'

def test_normalize_absolute_path():
    with patch('flutils.pathutils._normalize_path', return_value=Path('/usr/local/share/foo')):
        absolute_path = Path('/usr/local/bin/../share/foo')
        normalized_absolute_path = _normalize_path_pathlib(absolute_path)
        assert str(normalized_absolute_path) == '/usr/local/share/foo'

def test_normalize_env_var_path():
    with patch('flutils.pathutils._normalize_path', return_value=Path('/home/test_user/reports/data')):
        env_var_path = Path('~/documents/../reports/data')
        normalized_env_var_path = _normalize_path_pathlib(env_var_path)
        assert str(normalized_env_var_path) == '/home/test_user/reports/data'

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