
import pytest
from pathlib import Path
import os
from flutils.pathutils import normalize_path

# Test 1: Normalize a POSIX-style path (Unix/Linux)
def test_normalize_posix_path():
    normalized_path = normalize_path('~/tmp/foo/../bar')
    assert str(normalized_path) == '/home/test_user/tmp/bar'

# Test 2: Normalize a Windows-style path (Windows)
def test_normalize_windows_path():
    normalized_path = normalize_path('C:/Users/username/Documents/foo/../bar')
    assert str(normalized_path) == 'C:/Users/username/Documents/bar'

# Test 3: Normalize a byte string path (Unix/Linux)
def test_normalize_byte_string_path():
    normalized_path = normalize_path(b'~/tmp/foo/../bar'.encode('utf-8'))
    assert str(normalized_path) == '/home/test_user/tmp/bar'

# Test 4: Normalize a Windows byte string path (Windows)
def test_normalize_windows_byte_string_path():
    normalized_path = normalize_path(b'C:/Users/username/Documents/foo/../bar'.encode('utf-8'))
    assert str(normalized_path) == 'C:/Users/username/Documents/bar'

# Test 5: Normalize a Path object (Unix/Linux)
def test_normalize_path_object():
    raw_path = Path('~/tmp/foo/../bar')
    normalized_path = normalize_path(raw_path)
    assert str(normalized_path) == '/home/test_user/tmp/bar'

# Test 6: Normalize a Windows-style path (Windows)
def test_normalize_windows_path_object():
    raw_windows_path = Path('C:/Users/username/Documents/foo/../bar')
    normalized_path = normalize_path(raw_windows_path)
    assert str(normalized_path) == 'C:/Users/username/Documents/bar'

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