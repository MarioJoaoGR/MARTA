
import pytest
from flutils.objutils import is_subclass_of_any
from collections import ValuesView, KeysView, UserList

# Test 1: Checking if `dict` keys are a subclass of any specified classes
def test_is_subclass_of_any_with_dict_keys():
    obj = dict(a=1, b=2).keys()
    result = is_subclass_of_any(obj, ValuesView, KeysView, UserList)
    assert result == True

# Test 2: Checking if `list` is a subclass of any specified classes
def test_is_subclass_of_any_with_list():
    obj = [1, 2, 3].__class__
    result = is_subclass_of_any(obj, ValuesView, KeysView, UserList)
    assert result == False

# Test 3: Checking if `str` is a subclass of any specified classes
def test_is_subclass_of_any_with_str():
    obj = "example".__class__
    result = is_subclass_of_any(obj, ValuesView, KeysView, UserList)
    assert result == False

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