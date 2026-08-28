
import pytest
from unittest.mock import patch
from flutils.moduleutils import CherryPickError

def test_cherrypickerror_with_fullname_and_message():
    with pytest.raises(CherryPickError) as excinfo:
        raise CherryPickError("module.function", "An error occurred during cherry-picking.")
    
    assert str(excinfo.value) == "module.function.An error occurred during cherry-picking."

def test_cherrypickerror_with_different_fullname_and_message():
    with pytest.raises(CherryPickError) as excinfo:
        raise CherryPickError("another_module.another_function", "A different error occurred during cherry-picking.")
    
    assert str(excinfo.value) == "another_module.another_function.A different error occurred during cherry-ping."

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