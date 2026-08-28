
import pytest
from pathlib import Path
from flutils.pathutils import chmod

# Test for changing mode of a single file
def test_chmod_single_file():
    # Create a temporary file to change its mode
    temp_file = Path('temp_file.txt')
    temp_file.touch()
    
    try:
        chmod(str(temp_file), mode_file=0o644)
        assert temp_file.stat().st_mode == 0o644
    finally:
        temp_file.unlink()

# Test for changing mode of all files and directories within a directory recursively
def test_chmod_recursive():
    # Create a temporary directory structure to apply chmod patterns
    temp_dir = Path('temp_dir')
    temp_dir.mkdir()
    (temp_dir / 'file1.txt').touch()
    (temp_dir / 'subdir').mkdir()
    (temp_dir / 'subdir' / 'file2.txt').touch()
    
    try:
        chmod(str(temp_dir) + '/**', mode_file=0o644, mode_dir=0o755)
        assert (temp_dir / 'file1.txt').stat().st_mode == 0o644
        assert (temp_dir / 'subdir' / 'file2.txt').stat().st_mode == 0o644
        assert (temp_dir / 'subdir').stat().st_mode == 0o755
    finally:
        Path('temp_dir/file1.txt').unlink()
        Path('temp_dir/subdir/file2.txt').unlink()
        Path('temp_dir/subdir').rmdir()
        temp_dir.rmdir()

# Test for changing mode of immediate contents of a directory without recursion
def test_chmod_immediate_contents():
    # Create a temporary directory with files and directories
    temp_dir = Path('temp_dir')
    temp_dir.mkdir()
    (temp_dir / 'file1.txt').touch()
    (temp_dir / 'subdir').mkdir()
    
    try:
        chmod(str(temp_dir) + '/*', mode_file=0o644, mode_dir=0o755)
        assert (temp_dir / 'file1.txt').stat().st_mode == 0o644
        assert not (temp_dir / 'subdir').exists()
    finally:
        Path('temp_dir/file1.txt').unlink()
        Path('temp_dir/subdir').rmdir()
        temp_dir.rmdir()

# Test for including the parent directory in the chmod operation for glob patterns
def test_chmod_include_parent():
    # Create a temporary directory with files and directories
    temp_dir = Path('temp_dir')
    temp_dir.mkdir()
    (temp_dir / 'file1.txt').touch()
    (temp_dir / 'subdir').mkdir()
    
    try:
        chmod(str(temp_dir) + '/**', mode_file=0o644, mode_dir=0o755, include_parent=True)
        assert temp_dir.stat().st_mode == 0o755
    finally:
        Path('temp_dir/file1.txt').unlink()
        Path('temp_dir/subdir').rmdir()
        temp_dir.rmdir()

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