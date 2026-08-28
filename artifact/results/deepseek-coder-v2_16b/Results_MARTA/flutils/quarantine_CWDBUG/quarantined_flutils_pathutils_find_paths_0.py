
import pytest
from pathlib import Path
from flutils.pathutils import find_paths, normalize_path
import os

# Test 1: Basic Usage
def test_find_paths_basic():
    pattern = '~/tmp/*'
    normalized_pattern = Path(os.path.expanduser(pattern))
    expected_paths = list(normalized_pattern.glob('*'))
    
    paths = list(find_paths(pattern))
    
    assert len(paths) == len(expected_paths), f"Expected {len(expected_paths)} paths, but got {len(paths)}"
    for path in paths:
        assert path.is_absolute(), "Path is not absolute"
        assert path in expected_paths, f"Unexpected path found: {path}"

# Test 2: Pattern with Wildcards
def test_find_paths_wildcard():
    pattern = '~/tmp/?.txt'
    normalized_pattern = Path(os.path.expanduser(pattern))
    expected_paths = list(normalized_pattern.glob('*'))
    
    paths = list(find_paths(pattern))
    
    assert len(paths) == len(expected_paths), f"Expected {len(expected_paths)} paths, but got {len(paths)}"
    for path in paths:
        assert path.is_absolute(), "Path is not absolute"
        assert path in expected_paths, f"Unexpected path found: {path}"

# Test 3: Using an Absolute Path
def test_find_paths_absolute():
    pattern = '/home/user/data/*'
    normalized_pattern = Path(pattern)
    expected_paths = list(normalized_pattern.glob('*'))
    
    paths = list(find_paths(pattern))
    
    assert len(paths) == len(expected_paths), f"Expected {len(expected_paths)} paths, but got {len(paths)}"
    for path in paths:
        assert path.is_absolute(), "Path is not absolute"
        assert path in expected_paths, f"Unexpected path found: {path}"

# Test 4: Using a Relative Path
def test_find_paths_relative():
    pattern = 'data/*'
    normalized_pattern = normalize_path(pattern)
    expected_paths = list(Path.cwd().joinpath(normalized_pattern).glob('*'))
    
    paths = list(find_paths(pattern))
    
    assert len(paths) == len(expected_paths), f"Expected {len(expected_paths)} paths, but got {len(paths)}"
    for path in paths:
        assert path.is_absolute(), "Path is not absolute"
        assert path in expected_paths, f"Unexpected path found: {path}"

# Test 5: Handling Different Operating Systems
@pytest.mark.skipif(os.name != 'posix', reason="This test only runs on POSIX systems")
def test_find_paths_posix():
    pattern = '~/tmp/*'
    normalized_pattern = Path(os.path.expanduser(pattern))
    expected_paths = list(normalized_pattern.glob('*'))
    
    paths = list(find_paths(pattern))
    
    assert len(paths) == len(expected_paths), f"Expected {len(expected_paths)} paths, but got {len(paths)}"
    for path in paths:
        assert path.is_absolute(), "Path is not absolute"
        assert path in expected_paths, f"Unexpected path found: {path}"

@pytest.mark.skipif(os.name == 'posix', reason="This test only runs on Windows")
def test_find_paths_windows():
    pattern = 'C:/users/public/downloads/*'
    normalized_pattern = Path(pattern)
    expected_paths = list(normalized_pattern.glob('*'))
    
    paths = list(find_paths(pattern))
    
    assert len(paths) == len(expected_paths), f"Expected {len(expected_paths)} paths, but got {len(paths)}"
    for path in paths:
        assert path.is_absolute(), "Path is not absolute"
        assert path in expected_paths, f"Unexpected path found: {path}"

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