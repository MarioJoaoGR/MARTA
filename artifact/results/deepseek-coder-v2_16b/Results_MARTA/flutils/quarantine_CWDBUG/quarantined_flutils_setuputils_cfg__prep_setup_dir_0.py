
import os
import pytest
from inspect import stack as extract_stack
from types import FrameType
from typing import Optional, Union, cast

def _validate_setup_dir(path: str):
    if not os.path.exists(path) or not os.path.isdir(path):
        raise FileNotFoundError(f"The provided path '{path}' does not exist or is not a directory.")
    if not os.path.isfile(os.path.join(path, 'setup.py')):
        raise FileNotFoundError(f"The provided path '{path}' does not contain 'setup.py'.")

def _prep_setup_dir(
        setup_dir: Optional[Union[os.PathLike, str]] = None
) -> str:
    """The path to the directory that contains the project's ``setup.py``
    file.
    """
    if setup_dir:
        setup_dir = str(setup_dir)
        _validate_setup_dir(setup_dir)
        return os.path.realpath(setup_dir)

    for fs in extract_stack():
        fs = cast(FrameType, fs)
        basename = os.path.basename(fs.filename)
        if basename == 'setup.py':
            setup_dir = str(os.path.dirname(fs.filename))
            _validate_setup_dir(setup_dir)
            return os.path.realpath(setup_dir)
    raise FileNotFoundError(
        "Unable to find the directory that contains the 'setup.py' file."
    )

# Test cases for _prep_setup_dir function
def test_provided_explicit_path():
    setup_dir = os.path.abspath("tests/test_setup.py")
    result = _prep_setup_dir(setup_dir)
    assert os.path.exists(result), f"Expected directory does not exist: {result}"
    assert os.path.isdir(result), "The provided path is not a directory."
    assert os.path.isfile(os.path.join(result, 'setup.py')), "Directory does not contain 'setup.py'."

def test_default_search_mechanism():
    try:
        result = _prep_setup_dir()
        assert os.path.exists(result), "Expected directory does not exist."
        assert os.path.isdir(result), "The provided path is not a directory."
        assert os.path.isfile(os.path.join(result, 'setup.py')), "Directory does not contain 'setup.py'."
    except FileNotFoundError as e:
        pytest.fail(f"Unexpected FileNotFoundError: {e}")

def test_non_existent_path():
    with pytest.raises(FileNotFoundError):
        _prep_setup_dir("non/existent/path")

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